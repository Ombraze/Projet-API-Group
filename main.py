from fastapi import HTTPException, FastAPI
from data import champConvert, itemConvert
from Class.Champion import ShowChampion
from Class.Object.Item import Show_Item
from Class.Team import Team, TeamCreate


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
        return HTTPException(status_code=422, detail="Please input something")
    if id and name:
        return HTTPException(status_code=422, detail="Please search by either the Id or the Name")
    for e in champConvert.champions:
        if id is None:
            if e.name == name:
                return e
            
    for e in champConvert.champions:
        if name is None:
            if e.id == id:
                return e

@app.get("/items", response_model=list[Show_Item])
def getAllItems():
    return itemConvert.items

@app.get("/item")
def getItem(id: int | None = None, name: str | None = None):
    if id is None and name is None:
        return HTTPException(status_code=422, detail="Please input something")
    if id and name:
        return HTTPException(status_code=422, detail="Please search by either the Id or the Name")
    for e in itemConvert.items:
        if id is None:
            if e.name == name:
                return e
            
    for e in itemConvert.items:
        if name is None:
            if e.id == id:
                return e


#post requests
@app.post("/team", response_model=Team)
def createTeam(team_request: TeamCreate):

    if team_request.name is None:
        return HTTPException(status_code=422, detail="Please input a team name")
    selected_champions = []

    for champion_id in team_request.champion_ids:
        for champion in champConvert.champions:
            if champion.id == champion_id:
                selected_champions.append(champion)

    for champion_name in team_request.champion_name:
        for champion in champConvert.champions:
            if champion.name == champion_name:
                selected_champions.append(champion)

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
        return HTTPException(status_code=422, detail="Please input something")
    if id and name:
        return HTTPException(status_code=422, detail="Please search by either the Id or the Name")
    for index, teams in enumerate(Teams):
        if name is None:
            if teams.id == id:
                Teams.pop(index)
                return {"message": "successfully removed the team"}
    for index, teams in enumerate(Teams):
        if id is None:
            if teams.name == name:
                Teams.pop(index)
                return {"message": "successfully removed the team"}
    return {"message": "could not perform this action"}