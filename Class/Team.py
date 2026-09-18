from pydantic import BaseModel, Field

from Class.Champion import Champion


class Team(BaseModel):
    name: str = Field(...)
    Champions: list[Champion] = Field(default_factory=list, max_items=6, description="Nombre maximum de champions dans l'équipe")
