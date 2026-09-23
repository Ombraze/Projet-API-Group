from Class.champion import ChampionData
from Class.Object.item import ItemData

champConvert = ChampionData.model_validate_json(
    open("Data/champions.json", encoding="utf-8").read()
)

itemConvert = ItemData.model_validate_json(
    open("Data/items.json", encoding="utf-8").read()
)

champions = champConvert.champions
items = itemConvert.items

