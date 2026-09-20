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
        raise HTTPException(status_code=422, detail="Please input something")

    if id and name:
        raise HTTPException(status_code=422, detail="Please search by either the Id or the Name")

    for e in itemConvert.items:
        if id is None:
            if e.name == name:
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

#post requests
@app.post("/team", response_model=ShowTeam)
def createTeam(team_request: TeamCreate):
    if team_request.name is None:
        raise HTTPException(status_code=422, detail="Please input a team name")
    selected_champions = []

    for champion_id in team_request.champion_ids:
        for champion in champConvert.champions:
            if champion.id == champion_id:
                selected_champions.append(champion)

    for champion_name in team_request.champion_name:
        for champion in champConvert.champions:
            if champion.name == champion_name:
                selected_champions.append(champion)

    if not selected_champions:
        raise HTTPException(status_code=422, detail="Please pick at least one champion")

    for existing_team in Teams:
        if team_request.name == existing_team.name:
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
            if teams.name == name:
                Teams.pop(index)
                return {"message": "successfully removed the team"}
    return {"message": "could not perform this action"}