"""TCP Server (IPv4) - Non-Blocking Mode (I/O Multiplex)
"""

from __future__ import annotations

import logging
import selectors
import socket
from typing import NoReturn

from net import (
    get_tcp_server_max_connect_timeout,
    handle_listen,
    handle_reuse_address,
    handle_reuse_port,
    handle_socket_bufsize,
    handle_tcp_keepalive,
    handle_tcp_nodelay,
    handle_tcp_quickack,
)

logging.basicConfig(
    level=logging.DEBUG, style='{', format='[{processName} ({process})] {message}'
)
logger = logging.getLogger()

# In non-blocking mode: I/O multiplex
# on Windows and POSIX: select()
# on Linux 2.5.44+: epoll()
# on most UNIX system: poll()
# on BSD (including macOS): kqueue()
#
# @see select
selector = selectors.DefaultSelector()

recv_buf_size: int | None = None
send_buf_size: int | None = None
g_tcp_nodelay: bool | None = None
g_tcp_quickack: bool | None = None
g_tcp_keepalive_enabled = None
g_tcp_keepalive_idle = None
g_tcp_keepalive_cnt = None
g_tcp_keepalive_intvl = None


def handle_read(conn: socket.socket, mask: int) -> None:
    """Callback for read events."""
    assert mask == selectors.EVENT_READ

    try:
        client_address = conn.getpeername()

        data = conn.recv(1024)
        if data:
            logger.debug(f'recv: {data!r}, from {client_address}')
            conn.sendall(data)
            logger.debug(f'sent: {data!r}')
        else:
            logger.debug(f'no data from {client_address}')
            selector.unregister(conn)

            # explicitly shutdown.
            # `socket.close()` merely releases the socket
            # and waits for GC to perform the actual close.
            conn.shutdown(socket.SHUT_WR)
            conn.close()
    except OSError as err:
        logger.error(err)


def handle_requests(sock: socket.socket, mask: int) -> None:
    """Callback for new connections."""
    assert mask == selectors.EVENT_READ

    conn, client_address = sock.accept()
    assert isinstance(conn, socket.socket)
    logger.debug(f'recv request from {client_address}')

    handle_socket_bufsize(conn, recv_buf_size, send_buf_size)
    if g_tcp_nodelay is not None:
        handle_tcp_nodelay(conn, g_tcp_nodelay)
    if g_tcp_quickack is not None:
        handle_tcp_quickack(conn, g_tcp_quickack)

    handle_tcp_keepalive(
        sock,
        g_tcp_keepalive_enabled,
        g_tcp_keepalive_idle,
        g_tcp_keepalive_cnt,
        g_tcp_keepalive_intvl,
    )

    conn.setblocking(False)
    selector.register(conn, selectors.EVENT_READ, handle_read)


def run_server(
    host: str = '',
    port: int = 0,
    *,
    reuse_address: bool = True,
    reuse_port: bool = True,
    tcp_nodelay: bool = True,
    tcp_quickack: bool = True,
    accept_queue_size: int | None = None,
    timeout: float | None = None,
    tcp_keepalive: bool | None = None,
    tcp_keepalive_idle: int | None = None,
    tcp_keepalive_cnt: int | None = None,
    tcp_keepalive_intvl: int | None = None,
) -> NoReturn:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    handle_reuse_address(sock, reuse_address)
    handle_reuse_port(sock, reuse_port)
    handle_tcp_nodelay(sock, tcp_nodelay)
    global g_tcp_nodelay
    g_tcp_nodelay = tcp_nodelay

    global g_tcp_keepalive_enabled
    global g_tcp_keepalive_idle
    global g_tcp_keepalive_cnt
    global g_tcp_keepalive_intvl
    g_tcp_keepalive_enabled = tcp_keepalive
    g_tcp_keepalive_idle = tcp_keepalive_idle
    g_tcp_keepalive_cnt = tcp_keepalive_cnt
    g_tcp_keepalive_intvl = tcp_keepalive_intvl
    handle_tcp_keepalive(
        sock, tcp_keepalive, tcp_keepalive_idle, tcp_keepalive_cnt, tcp_keepalive_intvl
    )

    handle_tcp_quickack(sock, tcp_quickack)
    global g_tcp_quickack
    g_tcp_quickack = tcp_quickack

    # non-blocking mode: == sock.settimeout(0.0)
    sock.setblocking(False)

    # Bind
    sock.bind((host, port))
    server_address: tuple[str, int] = sock.getsockname()
    logger.debug(f'Server address: {server_address}')

    handle_listen(sock, accept_queue_size)

    selector.register(sock, selectors.EVENT_READ, handle_requests)

    logger.debug(f'max connect timeout: {get_tcp_server_max_connect_timeout()}')

    # Accept and handle incoming client requests
    try:
        while True:
            for key, mask in selector.select(timeout):
                callback = key.data
                callback(key.fileobj, mask)
    finally:
        sock.close()
        selector.close()


# host
# - 'localhost': socket.INADDR_LOOPBACK
# - '' or '0.0.0.0': socket.INADDR_ANY
# - socket.INADDR_BROADCAST
# Port 0 means to select an arbitrary unused port
run_server(
    'localhost',
    9999,
    timeout=5.5,
    tcp_keepalive=True,
    tcp_keepalive_idle=1800,
    tcp_keepalive_cnt=5,
    tcp_keepalive_intvl=15,
)
