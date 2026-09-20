from pydantic import BaseModel, Field
from Class.Champion import Champion
from Class.validators import nameValidator, teamChampionSelectionValidator

class Team(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    Champions: list[Champion] = Field(default_factory=list, max_length=6, description="Nombre maximum de champions dans l'équipe")

class TeamCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=69)
    champion_ids: list[int] = Field(default_factory=list, max_length=6)
    champion_name: list[str] = Field(default_factory=list, max_length=6)

    _validateName = nameValidator
    _validateChampionSelection = teamChampionSelectionValidator

class ShowTeam(BaseModel):
    name: str = Field(...)
    Champions: list[Champion] = Field(default_factory=list, max_length=6, description="Nombre maximum de champions dans l'équipe")
