"""Asynchronous I/O - coroutine.
"""

import asyncio
import logging
import sys

logging.basicConfig(
    level=logging.DEBUG, style='{', format='[{threadName} ({thread})] {message}'
)


async def coroutine(arg: int):
    logging.debug(f'run coroutine: {arg}')
    return arg + 1


coro = coroutine(1)
if sys.version_info >= (3, 7):  # Python 3.7+
    result = asyncio.run(coro)
    logging.debug(f'result: {result}')
else:
    # Low-level APIs
    # `get_running_loop()` has been added since Python 3.7.
    # `get_event_loop()` has been deprecated since Python 3.10.
    loop = asyncio.get_running_loop()
    try:
        logging.debug('starting event loop')
        result = loop.run_until_complete(coro)
        logging.debug(f'result: {result}')
    finally:
        loop.close()
