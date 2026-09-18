from Object.item import Item


class Consomable(Item):
    def __init__(
        self,
        id: int,
        nom: str,
        prix: int,
        description: str,
        categorie: str,
        role: str,
        statistiques: dict[str, float],
        tags: list[str],
        sub_item_ids: list[int] | None = None,
    ):
        super().__init__(
            id=id,
            nom=nom,
            prix=prix,
            description=description,
            categorie=categorie,
            role=role,
            statistiques=statistiques,
            tags=tags,
            sub_item_ids=sub_item_ids or [],
        )
