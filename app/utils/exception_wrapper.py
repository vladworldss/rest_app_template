import asyncio

from functools import wraps
from typing import Any, Callable, Type


def exception_wrapper_async(raised_exc: Type[Exception]) -> Callable:
    def decorator(fn: Callable) -> Callable:
        if not asyncio.iscoroutinefunction(fn):
            raise RuntimeError(f'Coroutine function is required, got {fn}')

        @wraps(fn)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return await fn(*args, **kwargs)
            except Exception as e:
                if isinstance(e, raised_exc):
                    raise e

                raise raised_exc(e)

        return wrapper

    return decorator


def exception_wrapper_sync(raised_exc: Type[Exception]) -> Callable:
    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                if isinstance(e, raised_exc):
                    raise e

                raise raised_exc(e)

        return wrapper

    return decorator
