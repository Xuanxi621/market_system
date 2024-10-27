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


class Goods(BaseModel):
    good_name: str = None
    price: float = None
    sales: int = None
    manufacture_date: str = None
    expiration_date: str = None


class Edit_Goods(BaseModel):
    id: int = None
    price: float = None
    sales: int = None
    manufacture_date: str = None
    expiration_date: str = None


@app.get("/")
async def sayHello():
    return {"Hello": "World"}


@app.post("/add_goods")
async def add_goods(goods: Goods):
    database_operate = dataBaseOperate('market.db')
    database_operate.insertGoods(goods.good_name, goods.price, goods.sales, goods.manufacture_date,
                                 goods.expiration_date)
    return 200


@app.post("/modify_goods")
async def modify_goods(edit_goods: Edit_Goods):
    database_operate = dataBaseOperate('market.db')
    database_operate.updateGoods(edit_goods.price, edit_goods.sales, edit_goods.manufacture_date,
                                 edit_goods.expiration_date, edit_goods.id)
    return 200


@app.get("/show_goods")
async def show_goods():
    return dataBaseOperate('market.db').selectGoodsList()


@app.get("/statistics")
async def statistics():
    return dataBaseOperate('market.db').selectGoodsOrderSales()


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
    # print(edit_pwd.password)
    # print(md5_encrypt(edit_pwd.password))
    try:
        user_id = database_operate.selectUserId(edit_pwd.name, md5_encrypt(edit_pwd.password))[0][0]
    except Exception as e:
        print(e)
        return 201
    database_operate.updateUserPwd(md5_encrypt(edit_pwd.new_password), user_id)
    return 200


if __name__ == '__main__':
    uvicorn.run(app="main:app", host='127.0.0.1', port=8100, reload=True)
