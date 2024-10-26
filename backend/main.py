import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from dataBase import dataBaseOperate
from MD5Util import md5_encrypt

app = FastAPI()


class User(BaseModel):
    name: str = None
    password: str = None


class Edit_Pwd(BaseModel):
    name: str = None
    password: str = None
    new_password: str = None


@app.get("/")
async def sayHello():
    return {"Hello": "World"}


@app.post("/login")
async def login(user: User):
    database_operate = dataBaseOperate('market.db')
    _user = database_operate.selectUser(user.name, md5_encrypt(user.password))
    if not _user:
        return 201
    return 200


@app.post("/register")
async def register(user: User):
    database_operate = dataBaseOperate('market.db')
    database_operate.insertUser(user.name, md5_encrypt(user.password))
    return 200


@app.post('/edit_pwd')
async def modify_pwd(edit_pwd: Edit_Pwd):
    database_operate = dataBaseOperate('market.db')
    print(edit_pwd.password)
    print(md5_encrypt(edit_pwd.password))
    try:
        user_id = database_operate.selectUserId(edit_pwd.name, md5_encrypt(edit_pwd.password))[0][0]
    except Exception as e:
        print(e)
        return 201
    database_operate.updateUserPwd(md5_encrypt(edit_pwd.new_password), user_id)
    return 200


if __name__ == '__main__':
    uvicorn.run(app="main:app", host='127.0.0.1', port=8100, reload=True)
