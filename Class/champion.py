from pydantic import BaseModel, Field

from Class.Lane import Lane
from Class.Role import Role
from Class.Object.Item import Item

class Champion(BaseModel):
    id: int = Field(..., description="L'id du champion")
    nom: str = Field(..., description="Le nom du champion")
    titre: str = Field(..., description="Le titre du champion")
    roles: list[Role] = Field(..., description="Les roles du champion")
    lanes: list[Lane] = Field(..., description="Les lanes du champion")
    stats: dict[str, int] = Field(..., description="Les statistiques du champion")
    ressource: str = Field(..., description="La ressource du champion")
    Items: list[Item] = Field(default_factory=list, max_items=6, description="Les items du champion, maximum 6")

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
