from typing import Type

from telegram.ext import Handler


def create_handler(handler_type: Type[Handler], *args, **kwargs):

    def decorator(callback) -> Handler:
        return handler_type(*args, **kwargs, callback=callback)

    return decorator
