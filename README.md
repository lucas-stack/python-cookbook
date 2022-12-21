# Python Cookbook

<section align="center">
  <img src="https://leven-cn.github.io/python-cookbook/imgs/python-logo.png"
    alt="Python Logo" width="250" height="250" style="text-align:center;" title="Python Logo">
  <br><br>
  <p>
    <a href="https://github.com/leven-cn/python-cookbook/actions/workflows/lint.yml">
      <img src="https://github.com/leven-cn/python-cookbook/actions/workflows/lint.yml/badge.svg"
      alt="GitHub Actions - lint" style="max-width:100%;">
    </a>
    <a href="https://github.com/pre-commit/pre-commit">
      <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"
      alt="pre-commit" style="max-width:100%;">
    </a>
  </p>
  <p>Recipes for <code>Python</code>. Hands-on code examples, snippets and guides for daily work.</p>
  <p><a href="https://leven-cn.github.io/python-cookbook/">https://leven-cn.github.io/python-cookbook/</a></p>
</section>

## Recipes

<!-- markdownlint-disable line-length -->

### Language Core (语言核心)

- Text Processing (文本处理)
  - [Universal Newline](https://leven-cn.github.io/python-cookbook/recipes/core/universal_newline)
  - [String format specification (字符串格式规范)](https://leven-cn.github.io/python-cookbook/recipes/core/str_fmt_spec)
  - [Regex Patterns](https://leven-cn.github.io/python-cookbook/recipes/core/regex_patterns)
- [Tuples with Named Fields - `namedtuple` (命名元组)](https://leven-cn.github.io/python-cookbook/recipes/core/namedtuple)
- [Ordered Dictionary - `OrderedDict`](https://leven-cn.github.io/python-cookbook/recipes/core/ordereddict)
- Decorator (装饰器)
  - [Function Decorator Without Argument](https://leven-cn.github.io/python-cookbook/recipes/core/function_decorator_no_args)
  - [Function Decorator With Required Arguments](https://leven-cn.github.io/python-cookbook/recipes/core/function_decorator_args_required)
  - [Function Decorator With Optional Arguments](https://leven-cn.github.io/python-cookbook/recipes/core/function_decorator_args_optional)
  - [Class Decorator](https://leven-cn.github.io/python-cookbook/recipes/core/class_decorator)
- Context Manager (上下文管理器)
  - [`with` Statement](https://leven-cn.github.io/python-cookbook/recipes/core/with_statement)
  - [Create Context Manager](https://leven-cn.github.io/python-cookbook/recipes/core/context_manager)
  - [Multiple Context Managers](https://leven-cn.github.io/python-cookbook/recipes/core/context_manager_multiple)
  - [Context Manager Protocol](https://leven-cn.github.io/python-cookbook/recipes/core/context_manager_protocol)
  - [Single Use Context Manager](https://leven-cn.github.io/python-cookbook/recipes/core/context_manager_single_use)
  - [Reentrant Context Manager](https://leven-cn.github.io/python-cookbook/recipes/core/context_manager_reentrant)
  - [Reusable Context Manager](https://leven-cn.github.io/python-cookbook/recipes/core/context_manager_reusable)
  - [Suppress Exceptions](https://leven-cn.github.io/python-cookbook/recipes/core/suppress_exceptions)
- Time
  - [Time: Timestamp (UNIX Time), UTC, Local Time](https://leven-cn.github.io/python-cookbook/recipes/core/time)
  - [Time Zone](https://leven-cn.github.io/python-cookbook/recipes/core/timezone)
- Representation of Dates and Times
  - [Format Date & Time String](https://leven-cn.github.io/python-cookbook/recipes/core/datetime_fmt_str)
  - [ISO 8601 Format](https://leven-cn.github.io/python-cookbook/recipes/core/datetime_fmt_iso_8601)
  - [RFC 3339 Format](https://leven-cn.github.io/python-cookbook/recipes/core/datetime_fmt_rfc_3339)
  - [RFC 5822/2822 Format](https://leven-cn.github.io/python-cookbook/recipes/core/datetime_fmt_rfc_2822)
- Type Hint / Type Annotation (类型提示/类型注解)
  - [Basic Types](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_basic_type)
  - [`namedtuple`: `typing.NamedTuple`](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_namedtuple)
  - [`itertools.chain`](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_itertools_chain)
  - [Literal: `typing.Literal`](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_literal)
  - [Union Types: `|`, ~~`typing.Union`~~, ~~`typing.Optional`~~](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_union)
  - [Any: `typing.Any` and `object`](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_any)
  - [Type objects](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_type)
  - [Callable objects](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_callable)
  - [Regex](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_regex)
  - [socket](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_socket)
  - [Constants and Class Attributes: `typing.Final`](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_constant)
  - [Class Variables: `typing.ClassVar`](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_class_var)
  - [Restricting Inheritance and Overriding: `@typing.final`](https://leven-cn.github.io/python-cookbook/recipes/core/type_hint_for_inheritance)
- [Pack/Unpack Binary Data - `struct`](https://leven-cn.github.io/python-cookbook/recipes/core/struct)
- I/O, File-Like Object
  - [Inheritance of File Descriptor](https://leven-cn.github.io/python-cookbook/recipes/core/fd_inheritable)
  - [Access Text Files](https://leven-cn.github.io/python-cookbook/recipes/core/text_io)
  - [Access Binary Files](https://leven-cn.github.io/python-cookbook/recipes/core/binary_io)
- Logging (日志)
  - [Logging Usage](https://leven-cn.github.io/python-cookbook/recipes/core/logging_usage)
  - [Logging Dictionary Configuration](https://leven-cn.github.io/python-cookbook/recipes/core/logging_dict_config)
- Command-Line Arguments Parser
  - [`argparse`](https://leven-cn.github.io/python-cookbook/recipes/core/argparse)
  - ~~`optparse`~~ (deprecated since Python *3.2*, use [`argparse`](https://leven-cn.github.io/python-cookbook/recipes/core/argparse) instead)
  - ~~`getopt`~~: C-Style Parser (use [`argparse`](<https://leven-cn.github.io/python-cookbook/recipes/core/argparse>) instead)
- Parallelism and Concurrent (并发)
  - [Multi-Threads Parallelism for **I/O-bound** tasks](https://leven-cn.github.io/python-cookbook/recipes/core/multi_threads)
  - [Multi-Processes Parallelism for **CPU-bound** tasks](https://leven-cn.github.io/python-cookbook/recipes/core/multi_processes)
  - [Multi-Processes - Queue (队列)](https://leven-cn.github.io/python-cookbook/recipes/core/multi_processes_queue)
  - [Process Pool](https://leven-cn.github.io/python-cookbook/recipes/core/process_pool)
  - [High-Level Threads-Based Concurrent](https://leven-cn.github.io/python-cookbook/recipes/core/concurrent_threads)
  - [High-Level Processes-Based Concurrent](https://leven-cn.github.io/python-cookbook/recipes/core/concurrent_processes)
  - [Synchronization Primitives - `Event` (For Processes and Threads)](https://leven-cn.github.io/python-cookbook/recipes/core/synchronization_event)
  - [Synchronization Primitives - Mutex Lock (互斥锁): `Lock` (For Processes and Threads)](https://leven-cn.github.io/python-cookbook/recipes/core/synchronization_lock)
  - [Synchronization Primitives - Reentrant Lock (重入锁): `RLock`](https://leven-cn.github.io/python-cookbook/recipes/core/synchronization_rlock)
  - [Synchronization Primitives - Condition Variable (条件变量): `Condition` (For Processes and Threads)](https://leven-cn.github.io/python-cookbook/recipes/core/synchronization_condition)
  - [Synchronization Primitives - Semaphore (信号量): `Semaphore` / `BoundedSemaphore` (For Processes and Threads)](https://leven-cn.github.io/python-cookbook/recipes/core/synchronization_semaphore)
  - [Synchronization Primitives - (栅栏): `Barrier`](https://leven-cn.github.io/python-cookbook/recipes/core/synchronization_barrier)
- Networks and Communications (网络通信)
  - [`socketserver` Class Diagram](https://leven-cn.github.io/python-cookbook/recipes/core/socketserver_class_diagram)
  - [TCP Server (IPv4) - Standard Framework](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_server_ipv4_std)
  - [TCP Server (IPv4) - Blocking Mode (阻塞模式)](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_server_ipv4_blocking)
  - [TCP Server (IPv4) - Timeout Mode](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_server_ipv4_timeout)
  - [TCP Server (IPv4) - Non-Blocking Mode (I/O Multiplex, I/O多路复用)](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_server_ipv4_io_multiplex)
  - [TCP Client (IPv4) - Basic](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_client_ipv4_basic)
  - [TCP Client (IPv4) - Timeout Mode](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_client_ipv4_timeout)
  - [TCP Client (IPv4) - Non-Blocking Mode (I/O Multiplex, I/O多路复用)](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_client_ipv4_io_multiplex)
  - [TCP Connect Timeout (Server Side)](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_connect_timeout_server)
  - [TCP Connect Timeout (Client Side)](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_connect_timeout_client)
  - [TCP Data Transmission Timeout](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_transmission_timeout)
  - [TCP `listen()` Queue](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_listen_queue)
  - [TCP Nodelay (Disable Nagle's Algorithm)](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_nodelay)
  - [TCP Keep-Alive](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_keepalive)
  - [TCP Quick ACK (Disable Delayed ACK (延迟确认))](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_quickack)
  - [UDP Server (IPv4) - Standard Framework](https://leven-cn.github.io/python-cookbook/recipes/core/udp_server_ipv4_std)
  - [UDP Server (IPv4) - Timeout Mode](https://leven-cn.github.io/python-cookbook/recipes/core/udp_server_ipv4_timeout)
  - [UDP Client (IPv4) - Timeout Mode](https://leven-cn.github.io/python-cookbook/recipes/core/udp_client_ipv4_timeout)
  - [TCP/UDP Reuse Address](https://leven-cn.github.io/python-cookbook/recipes/core/net_reuse_address)
  - [TCP/UDP Reuse Port](https://leven-cn.github.io/python-cookbook/recipes/core/net_reuse_port)
  - [TCP/UDP (Recv/Send) Buffer Size](https://leven-cn.github.io/python-cookbook/recipes/core/net_buffer_size)
  - [Create IP Multicast (组播) Server and Client (UDP)](https://leven-cn.github.io/python-cookbook/recipes/core/ip_multicast)
  - [IPC - Socket Pair](https://leven-cn.github.io/python-cookbook/recipes/core/ipc_socketpair)
  - [IPC - UNIX Domain Socket (UDS, UNIX 域套接字) Server and Client](https://leven-cn.github.io/python-cookbook/recipes/core/ipc_unix_domain_socket)
- Asynchronous I/O (异步 I/O)
  - [Coroutine (协程)](https://leven-cn.github.io/python-cookbook/recipes/core/asyncio_coroutine)
  - [Chain coroutines (串链协程)](https://leven-cn.github.io/python-cookbook/recipes/core/asyncio_coroutine_chain)
  - [Run coroutines Concurrently (并发执行协程)](https://leven-cn.github.io/python-cookbook/recipes/core/asyncio_coroutine_chain)
  - [Scheduled Tasks (调度任务)](https://leven-cn.github.io/python-cookbook/recipes/core/asyncio_schedule)
  - [Wait](https://leven-cn.github.io/python-cookbook/recipes/core/asyncio_wait)
  - [Nonblocking Main Thread](https://leven-cn.github.io/python-cookbook/recipes/core/asyncio_nonblocking)
  - [Synchronization Primitives: Lock](https://leven-cn.github.io/python-cookbook/recipes/core/asyncio_synchronization_lock)
  - [Synchronization Primitives: Event](https://leven-cn.github.io/python-cookbook/recipes/core/asyncio_synchronization_event)
  - [Synchronization Primitives: Condition](https://leven-cn.github.io/python-cookbook/recipes/core/asyncio_synchronization_condition)
  - [Synchronization Primitives: Semapore (信号量)](https://leven-cn.github.io/python-cookbook/recipes/core/asyncio_synchronization_semapore)
  - [Queue (队列)](https://leven-cn.github.io/python-cookbook/recipes/core/asyncio_queue)
  - [TCP Server (High-Level APIs)](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_server_asyncio_high_api)
  - [TCP Server (Low-Level APIs)](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_server_asyncio_low_api)
  - [TCP Client - (High-Level APIs)](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_client_asyncio_high_api)
  - [TCP Client - (Low-Level APIs)](https://leven-cn.github.io/python-cookbook/recipes/core/tcp_client_asyncio_low_api)
  - [UDP Server](https://leven-cn.github.io/python-cookbook/recipes/core/udp_server_asyncio)
  - [UDP Client](https://leven-cn.github.io/python-cookbook/recipes/core/udp_client_asyncio)
- Test
  - [`unittest` (Builtin)](https://leven-cn.github.io/python-cookbook/recipes/core/unittest)
  - [`pytest`](https://leven-cn.github.io/python-cookbook/recipes/core/pytest)
- Package Management
  - [`pip` - Standard Package Manager](https://leven-cn.github.io/python-cookbook/recipes/core/pip)
  - [`pipx` - Install and Run Python Applications](https://leven-cn.github.io/python-cookbook/recipes/core/pipx)
  - [`pipenv` - Virtual Environment Manager](https://leven-cn.github.io/python-cookbookbook/recipes/core/pipenv)
- [Setup Python Project](https://leven-cn.github.io/python-cookbook/recipes/core/python_project)
- [Performance Measurement](https://leven-cn.github.io/python-cookbook/recipes/core/perf)

### Web Development

- [URL Parsing: `urllib.parse`](https://leven-cn.github.io/python-cookbook/recipes/web/url_parse)
- [HTTP Range Requests: `Range`](https://leven-cn.github.io/python-cookbook/recipes/web/http_range)
- [HTTP Caching](https://leven-cn.github.io/python-cookbook/recipes/web/http_caching)
- [HTTP Datetime Format](https://leven-cn.github.io/python-cookbook/recipes/web/http_datetime_fmt)
- HTTP Server
  - [Builtin: `http.server`](https://leven-cn.github.io/python-cookbook/recipes/web/http_server_builtin)
  - Asyncio API: `aiohttp`
  - [HTTP Cookie (Server Side): `http.cookies`](https://leven-cn.github.io/python-cookbook/recipes/web/http_cookie)
- HTTP Client
  - [Builtin: `urllib.request`](https://leven-cn.github.io/python-cookbook/recipes/web/http_request)
  - `Postman` (GUI)
  - `requests` (using `urllib3`) (API)
  - Asyncio API: `aiohttp`
- [WSGI](https://leven-cn.github.io/python-cookbook/recipes/web/wsgi)
- **CGI** (deprecated since Python *3.11*, [use WSGI instead](https://leven-cn.github.io/python-cookbook/recipes/web/wsgi))
- Web Frameworks
  - Django
  - Flask
  - FastAPI
- Django
  - [Django - Quick Start](https://leven-cn.github.io/python-cookbook/recipes/web/django_quickstart)
  - [Django DB - PostgreSQL](https://leven-cn.github.io/python-cookbook/recipes/web/django_db_postgresql)
  - [Django Cache - Redis](https://leven-cn.github.io/python-cookbook/recipes/web/django_cache_redis)
  - [Django Logging](https://leven-cn.github.io/python-cookbook/recipes/web/django_logging)
- PostgreSQL
  - [PostgreSQL - Setup](https://leven-cn.github.io/python-cookbook/recipes/web/postgresql_setup)
  - [PostgreSQL CLI - Usage](https://leven-cn.github.io/python-cookbook/recipes/web/postgresql_usage)
  - PostgreSQL GUI (Official): `pgadmin4`
- Redis
  - [Redis - Setup](https://leven-cn.github.io/python-cookbook/recipes/web/redis_setup)
  - [Redis CLI - Basic Usage](https://leven-cn.github.io/python-cookbook/recipes/web/redis_usage_basic)
  - Redis GUI (Official): `RedisInsight`
  - Redis GUI (Official): `Redis Desktop Manager` (**deprecated**)
  - Redis GUI (Free): `Another Redis Desktop Manager`
  - [Redis Python API: `redis-py`](https://leven-cn.github.io/python-cookbook/recipes/web/redis)
  - Redis ORM: `pyton-redis-orm`
- Web Server
  - `uWSGI`

<!-- markdownlint-enable line-length -->

## More Details

### Core

- [Function (Method) Decorator](https://leven-cn.github.io/python-cookbook/more/core/function_decorator)
- [Representation of Dates and Times - ISO 8601 Format](https://leven-cn.github.io/python-cookbook/more/core/iso_8601_fmt)
- [Type Hint](https://leven-cn.github.io/python-cookbook/more/core/type_hint)
- [Logging Components and Flow](https://leven-cn.github.io/python-cookbook/more/core/logging)
- Networks and Communications (网络通信)
  - [Endianness](https://leven-cn.github.io/python-cookbook/more/core/endianness)
  - [TCP Slow Start (慢启动)](https://leven-cn.github.io/python-cookbook/more/core/tcp_slowstart)
  - [TCP RFC 1337 - TIME-WAIT Assassination Hazards (TIME-WAIT 暗杀)](https://leven-cn.github.io/python-cookbook/more/core/tcp_rfc1337)
  - [TCP Selective ACK](https://leven-cn.github.io/python-cookbook/more/core/tcp_sack)

### Web

- [URL, URI, URN](https://leven-cn.github.io/python-cookbook/more/web/uri_url_urn)
- [HTTP Basic](https://leven-cn.github.io/python-cookbook/more/web/http_basic)
- [HTTP Connection Management](https://leven-cn.github.io/python-cookbook/more/web/http_connection)
- [HTTP Authentication](https://leven-cn.github.io/python-cookbook/more/web/http_authentication)
- [HTTP Cookie](https://leven-cn.github.io/python-cookbook/more/web/http_cookie)
- [Cross-Site Request Forgery (CSRF) (跨站请求伪造)](https://leven-cn.github.io/python-cookbook/more/web/csrf)

See [full-version documentation](https://leven-cn.github.io/)

## License

[Apache 2.0 License](https://github.com/leven-cn/python-cookbook/blob/main/LICENSE)
