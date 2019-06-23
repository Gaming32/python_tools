"A group of modules to aid you in python programming"
from . import tools
from .tools import *

__all__ = ['tools', 'dictionary', 'filestor', 'lister', 'matrices', 'path', 'tkwidg'] + [x for x in dir(tools) if x[0] != '_']