from .lib.my_project_core import Calculator
from .version import __version__

__all__ = ["Calculator", "__version__"]


def hello() -> str:
    return "Hello from my_project!"
