from functools import wraps
import logging.config
from inspect import currentframe, getouterframes

logger = logging.getLogger(__name__)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        caller = getouterframes(currentframe())[1][3]
        logger.info(f'function named {func.__name__} call, argument {args}, {kwargs}. call from {caller}.')
        return func(*args, **kwargs)

    return wrapper

