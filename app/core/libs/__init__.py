import enum

class RandomType(enum.Enum):
    STRING: str = 'S'
    INTEGER: str = 'I'

class LogLevel(enum.Enum):
    DEBUG: str = 'D'
    INFO: str = 'I'
    WARNING: str = 'W'
    ERROR: str = 'E'
    CRITICAL: str = 'C'