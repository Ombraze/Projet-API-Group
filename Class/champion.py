from pydantic import BaseModel, Field


class champion (BaseModel):
    id: int = Field(..., description="L'id du champion")
    nom: str = Field(..., description="Le nom du champion")
    titre: str = Field(..., description="Le titre du champion")
    roles: list[str] = Field(..., description="Les roles du champion")
    ressourc