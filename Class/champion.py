from pydantic import BaseModel, Field


class Champion(BaseModel):
    id: int = Field(..., description="L'id du champion")
    nom: str = Field(..., description="Le nom du champion")
    titre: str = Field(..., description="Le titre du champion")
    roles: list[str] = Field(..., description="Les roles du champion")
    ressource: str

#request model
class ShowChampion(BaseModel):
    nom: str = Field(..., description="Le nom du champion")
    titre: str = Field(..., description="Le titre du champion")
    roles: list[str] = Field(..., description="Les roles du champion")
    ressource: str

#loader class
class ChampionData(BaseModel):
    patch: str
    source: str
    carte: str
    count: int
    champions: list[Champion]