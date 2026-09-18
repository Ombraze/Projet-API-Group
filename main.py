from fastapi import HTTPException, FastAPI

app = FastAPI()


@app.get("/")
def homePage():
    return "bonjour"

