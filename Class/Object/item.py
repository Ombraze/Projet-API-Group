from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int = Field(..., description="L'id de l'item")
    nom: str = Field(..., description="Le nom de l'item")
    prix: int = Field(..., description="Le prix de l'item")
    description: str = Field(..., description="La description de l'item")
    categorie: str = Field(..., description="La categorie de l'item")
    role: str = Field(..., description="Le role de l'item")
    statistiques: dict[str, float] = Field(..., description="Les statistiques de l'item")
    tags: list[str] = Field(default_factory=list, description="Les tags de l'item")
    sub_item_ids: list[int] = Field(default_factory=list, description="Les ids des composants de l'item")

#request model
class Show_Item(BaseModel):
    nom: str = Field(..., description="Le nom de l'item")
    prix: int = Field(..., description="Le prix de l'item")
    description: str = Field(..., description="La description de l'item")
    categorie: str = Field(..., description="La categorie de l'item")
    role: str = Field(..., description="Le role de l'item")
    statistiques: dict[str, float] = Field(..., description="Les statistiques de l'item")
    tags: list[str] = Field(default_factory=list, description="Les tags de l'item")
    sub_item_ids: list[int] = Field(default_factory=list, description="Les ids des composants de l'item")

#loader class
class ItemData(BaseModel):
    patch: str
    source: str
    carte: str
    filtre: str
    count: int
    items: list[Item]


class ItemList(BaseModel):
    items: list[Item]
    def __init__(self, items: list[Item]):
        self.items = items
    def add_item(self, item: Item):
        self.items.append(item)
    def remove_item(self, item: Item):
        self.items.remove(item)
    def get_item(self, id: int):
        return next((item for item in self.items if item.id == id), None)
    def get_items(self):
        return self.items
    def get_item_by_name(self, name: str):
        return next((item for item in self.items if item.name == name), None)
