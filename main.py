from fastapi import HTTPException, FastAPI
from data import champConvert, itemConvert
from Class.Champion import ShowChampion
from Class.Object.Item import Show_Item
from Class.Team import Team, TeamCreate, ShowTeam


app = FastAPI()

Teams: list[Team] = []


#get requests
@app.get("/")
def homePage():
    return "bonjour"

@app.get("/champions", response_model=list[ShowChampion])
def getAllChampions():
    return champConvert.champions

@app.get("/champion")
def getChampion(id: int | None = None, name: str | None = None):
    if id is None and name is None:
        raise HTTPException(status_code=422, detail="Please input something")

    if id and name:
        raise HTTPException(status_code=422, detail="Please search by either the Id or the Name")

    for e in champConvert.champions:
        if id is None:
            if e.name.lower() == name.lower():
                return e
            
    for e in champConvert.champions:
        if name is None:
            if e.id == id:
                return e

@app.get("/items", response_model=list[Show_Item])
def getAllItems():
    return itemConvert.items

@app.get("/filterItems", response_model=list[Show_Item])
def filterItems(categorie: str | None = None, limit: int | None = None, offset: int = 0, sort_by: str | None = None,):
    if limit is not None and limit < 1:
        raise HTTPException(status_code=422, detail="limit needs to be higher than zero")
    if offset < 0:
        raise HTTPException(status_code=422, detail="offset can't be negative")

    selected_items = itemConvert.items

    if categorie is not None:
        selected_items = [
            item for item in selected_items
            if item.categorie.lower() == categorie.lower()
        ]

    if sort_by is not None:
        sortalbe = {"name", "prix", "categorie", "role"}
        if sort_by not in sortalbe:
            raise HTTPException(status_code=422, detail="invalid sort field")
        selected_items = sorted(
            selected_items,
            key=lambda item: getattr(item, sort_by),
        )

    if limit is None:
        return selected_items[offset:]
    return selected_items[offset:offset + limit]

@app.get("/stats")
def itemGlobalStats():
    totalItems = len(itemConvert.items)

    totalPrice = 0
    for item in itemConvert.items:
        totalPrice = totalPrice + item.prix
    
    if totalItems > 0:
        averagePrice = totalPrice / totalItems
    else:
        averagePrice = 0

    categoryCounts = {}
    for item in itemConvert.items:
        if item.categorie in categoryCounts:
            categoryCounts[item.categorie] = categoryCounts[item.categorie] + 1
        else:
            categoryCounts[item.categorie] = 1

    mostCommon = None
    bestCount = 0
    for categorie, count in categoryCounts.items():
        if count > bestCount:
            bestCount = count
            mostCommon = categorie

    return {
        "total items": totalItems,
        "average price": averagePrice,
        "most common category": mostCommon,
    }

@app.get("/item")
def getItem(id: int | None = None, name: str | None = None):
    if id is None and name is None:
        raise HTTPException(status_code=422, detail="Please input something")

    if id and name:
        raise HTTPException(status_code=422, detail="Please search by either the Id or the Name")

    for e in itemConvert.items:
        if id is None:
            if e.name.lower() == name.lower():
                return e
            
    for e in itemConvert.items:
        if name is None:
            if e.id == id:
                return e

@app.get("/teams", response_model=list[ShowTeam])
def getAllTeams():
    if not Teams:
        raise HTTPException(status_code=404, detail="no teams exist")
    return Teams

@app.get("/team", response_model=ShowTeam)
def getTeam(name: str):
    if name is None:
        raise HTTPException(status_code=422, detail="Please input something")

    for existing_team in Teams:
        if existing_team.name.lower() == name.lower():
            return existing_team
    raise HTTPException(status_code=404, detail="No such team exists")

#post requests
@app.post("/team", response_model=ShowTeam)
def createTeam(team_request: TeamCreate):
    if team_request.name is None:
        raise HTTPException(status_code=422, detail="Please input a team name")
    selected_champions = []

    for champion_id in team_request.champion_ids:
        for champion in champConvert.champions:
            if champion.id == champion_id:
                selected_champions.append(champion.model_copy(deep=True))

    for champion_name in team_request.champion_name:
        for champion in champConvert.champions:
            if champion.name == champion_name:
                selected_champions.append(champion.model_copy(deep=True))

    if not selected_champions:
        raise HTTPException(status_code=422, detail="Please pick at least one champion")

    for existing_team in Teams:
        if team_request.name.lower() == existing_team.name.lower():
            raise HTTPException(status_code=409, detail="Team name already exists")

    next_id = len(Teams) + 1
    team = Team(
        id=next_id,
        name=team_request.name,
        Champions=selected_champions,
    )
    Teams.append(team)
    return team

#delete requests
@app.delete("/team")
def deleteTeam(id: int | None = None, name: str | None = None):
    if id is None and name is None:
        raise HTTPException(status_code=422, detail="Please input something")

    if id and name:
        raise HTTPException(status_code=422, detail="Please search by either the Id or the Name")

    for index, teams in enumerate(Teams):
        if name is None:
            if teams.id == id:
                Teams.pop(index)
                return {"message": "successfully removed the team"}

    for index, teams in enumerate(Teams):
        if id is None:
            if teams.name.lower() == name.lower():
                Teams.pop(index)
                return {"message": "successfully removed the team"}
    return {"message": "could not perform this action"}

#patch requests
@app.patch("/add", response_model=ShowTeam)
def addItem(team_name: str, champion_name: str, item_name: str):
    for existing_team in Teams:
        if existing_team.name.lower() == team_name.lower():
            selected_team = existing_team
            break
    else:
        raise HTTPException(status_code=404, detail="team does not exist")

    for existing_champion in selected_team.Champions:
        if existing_champion.name.lower() == champion_name.lower():
            selected_champion = existing_champion
            break
    else:
        raise HTTPException(status_code=404, detail="the champion does not exist in this team")

    for existing_item in itemConvert.items:
        if existing_item.name.lower() == item_name.lower():
            selected_item = existing_item
            break
    else:
        raise HTTPException(status_code=404, detail="this item does not exist")

    if len(selected_champion.Items) >= 6:
        raise HTTPException(status_code=422, detail="this champion already has six items")

    for held_item in selected_champion.Items:
        if held_item.id == selected_item.id:
            raise HTTPException(status_code=409, detail="item is already held")

    selected_champion.Items.append(selected_item.model_copy(deep=True))
    return selected_team


    