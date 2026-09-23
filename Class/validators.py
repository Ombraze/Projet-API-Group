from pydantic import field_validator, model_validator


def validateNonBlank(value: str):
    cleanedValue = value.strip()
    if not cleanedValue:
        raise ValueError("value cannot be blank")
    return cleanedValue


def validateName(cls, value: str):
    return validateNonBlank(value)


def validateTeamChampionSelection(self):
    if not self.champion_ids and not self.champion_name:
        raise ValueError("at least one champion must be selected")
    if len(self.champion_ids) + len(self.champion_name) > 6:
        raise ValueError("a team cannot contain more than six champions")
    return self


def validateItemComponents(self):
    if self.id in self.sub_item_ids:
        raise ValueError("an item cannot be one of its own components")
    return self


nameValidator = field_validator("name")(validateName)
teamChampionSelectionValidator = model_validator(mode="after")(validateTeamChampionSelection)
itemComponentsValidator = model_validator(mode="after")(validateItemComponents)