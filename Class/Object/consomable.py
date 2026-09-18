from Object.Item import Activable, Item


class Consomable(Item):
    def __init__(
        self,
        id: int,
        nom: str,
        prix: int,
        description: str,
        statistiques: dict[str, float],
        tags: list[str],
    ):
        super().__init__(
            id=id,
            nom=nom,
            prix=prix,
            description=description,
            statistiques=statistiques,
            tags=tags,
            activable=Activable.NO,
        )
