from fastapi import HTTPException, FastAPI
from data import champConvert, itemConvert
from Class.champion import ShowChampion
from Class.Object.item import Show_Item

app = FastAPI()



#get requests
@app.get("/")
def homePage():
    return "bonjour"

@app.get("/champions", response_model=list[ShowChampion])
def getAllChampions():
    return champConvert.champions

@app.get("/items", response_model=list[Show_Item])
def getAllItems():
    return itemConvert.items