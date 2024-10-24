from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def sayHello():
    return {"Hello": "World"}
