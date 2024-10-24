import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str = None
    password: str = None


@app.get("/")
async def sayHello():
    return {"Hello": "World"}

@app.post("/login")
async def login():
    pass


@app.post("/register")
async def register(user:User):
    return user
if __name__ == '__main__':
    uvicorn.run(app="main:app", host='127.0.0.1', port=8100, reload=True)



