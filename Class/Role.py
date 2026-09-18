from enum import Enum
from pydantic import Field

class Role(Enum):
    FIGHT = "fight"
    MARKSMAN = "marksman"
    SUPPORT = "support"
    TANK = "tank"
    MAGE = "mage"
    ASSASSIN = "assassin"

class RoleList(Enum):
    ROLES = [Role.FIGHT, Role.SUPPORT, Role.TANK, Role.MAGE, Role.ASSASSIN, Role.MARKSMAN]
    def get_role(self, type: str):
        return next((role for role in self.ROLES if role.value == type), None)
    def get_roles(self):
        return self.ROLES