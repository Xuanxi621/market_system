import sqlite3
from MD5Util import md5_encrypt


class dataBase:
    def __init__(self, dbname):
        self.common = sqlite3.connect(dbname)
        self.cur = self.common.cursor()

    def userDataBase(self):
        create_user_sql = """
            create table if not exists users(
                id integer primary key autoincrement,
                name text,
                password text,
                role integer
            )
        """
        self.cur.execute(create_user_sql)

    def goodsDataBase(self):
        create_goods_sql = """
            create table if not exist goods(
                id integer primary key autoincrement,
                goods_name text,
                price float,
                sales int,
                manufacture_date integer,
                expiration_date integer
            )
        """
        self.cur.execute(create_goods_sql)


class dataBaseOperate(dataBase):
    def __init__(self, dbname):
        super().__init__(dbname)
        self.userDataBase()
        self.goodsDataBase()

    def insertGoods(self, _goods_name, _price, _sales, _manufacture_date, _expiration_date):
        insert_goods_sql = """
            insert into goods(goods_name,price,sales,manufacture_date,expiration_date) values('%s','%f','%d','%d','%d')
        """ % (_goods_name, _price, _sales, _manufacture_date, _expiration_date)

        self.cur.execute(insert_goods_sql)
        self.common.commit()
        self.common.close()

    def insertUser(self, _name, _password):
        insert_user_sql = """
            insert into users(name,password,role) values('%s','%s',1)
        """ % (_name, _password)

        self.cur.execute(insert_user_sql)
        self.common.commit()
        self.common.close()

    def selectGoodsList(self):
        select_goods_sql = """
            select * from goods
        """

        self.cur.execute(select_goods_sql)
        return self.cur.fetchall()

    def selectUserList(self):
        select_user_sql = """
            select * from users
        """

        self.cur.execute(select_user_sql)
        return self.cur.fetchall()

    def selectUser(self, _name, _password):
        select_user_sql = """
            select * from users where name='%s' and password = '%s'
        """ % (_name, _password)

        self.cur.execute(select_user_sql)
        return self.cur.fetchall()

    def deleteUser(self):
        del_user_sql = """
            delete from users where id = 1
        """

        self.cur.execute(del_user_sql)

    def updateUserPwd(self, _password, _id):
        update_user_sql = """
            update users set password = '%s' where id = '%d'
        """ % (_password, _id)

        self.cur.execute(update_user_sql)
        self.common.commit()
        self.common.close()

    def updateGoods(self, _price, _sales, _manufacture_date, _expiration_date, _id):
        update_goods_sql = """
            update goods set price = '%f',sales='%d',manufacture_date='%d', expiration_date='%d' where id = '%d'
        """ % (_price, _sales, _manufacture_date, _expiration_date, _id)

        self.cur.execute(update_goods_sql)
        self.common.commit()
        self.common.close()

    def selectUserId(self, _name, _password):
        select_userid_sql = """
            select id from users where name='%s' and password = '%s'
        """ % (_name, _password)

        self.cur.execute(select_userid_sql)
        return self.cur.fetchall()

    def selectGoodsId(self, _goods_name):
        select_goodsId_sql = """
            select id from goods where goods_name='%s'
        """ % _goods_name

        self.cur.execute(select_goodsId_sql)
        return self.cur.fetchall()


if __name__ == '__main__':
    data_operate = dataBaseOperate("market.db")
    # data_operate.insertUser("string123", md5_encrypt("string"))
    # data_operate.deleteUser()
    # data_operate.common.commit()
    # users = data_operate.selectUserList()
    # user = data_operate.selectUserId("string123", md5_encrypt("string"))[0][0]
    # data_operate.common.close()
