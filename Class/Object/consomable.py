from Object.Item import Activable, Item


class Consomable(Item):
    def __init__(
        self,
        id: int,
        name: str,
        prix: int,
        description: str,
        statistiques: dict[str, float],
        tags: list[str],
    ):
        super().__init__(
            id=id,
            name=name,
            prix=prix,
            description=description,
            statistiques=statistiques,
            tags=tags,
            activable=Activable.NO,
        )
