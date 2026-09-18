from pydantic import  Field
from enum import Enum

class Lane(Enum):
    TOP = "top"
    JGL = "jgl"
    MID = "mid"
    ADC = "adc"
    SUP = "sup"

class LaneList(Enum):
    ROLES = [Role.TOP, Role.JGL, Role.MID, Role.ADC, Role.SUP]
    def get_role(self, type: str):
        return next((role for role in self.ROLES if role.value == type), None)
    