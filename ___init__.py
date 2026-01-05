"""
CleverMachine. A learning Chat Bot
"""

__version__ = "1.0 Alpha"
__author__ = "CleverMachine"

from .brain import CleverBrain
from .memory import MemoryManager
from .nlp import TextProcessor
from .personality import PersonalityManager

__all__ = ['CleverBrain', 'MemoryManager', 'TextProcessor', 'PersonalityManager']
