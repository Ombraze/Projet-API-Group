from pydantic import  Field
from enum import Enum

class Lane(Enum):
    TOP = "top"
    JGL = "jgl"
    MID = "mid"
    ADC = "adc"
    SUP = "sup"

class LaneList(Enum):
    LANE = [Lane.TOP, Lane.JGL, Lane.MID, Lane.ADC, Lane.SUP]
    def get_role(self, type: str):
        return next((role for role in self.LANE if role.value == type), None)
    