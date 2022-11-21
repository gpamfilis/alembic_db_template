from enum import Enum

class FlowType(Enum):
    RECCURING='recurring'
    ONEOFF = 'oneoff'

class UseType(Enum):
    PERSONAL = 'personal'
    BUSINESS = 'business'

class DirectionType(Enum):
    INFLOW = 'inflow'
    OUTFLOW = 'outflow'