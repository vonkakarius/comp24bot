from typing import Type, Callable

from telegram.ext import Handler


def create_handler(handler_type: Type[Handler], *args, **kwargs):
    """Transforms a callback into a handler that can be added to a python-telegram-bot application."""

    def decorator(callback: Callable) -> Handler:
        return handler_type(*args, **kwargs, callback=callback)

    return decorator
