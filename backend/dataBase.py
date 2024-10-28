import sqlite3


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
            create table if not exists goods(
                id integer primary key autoincrement,
                goods_name text,
                price float,
                sales int,
                manufacture_date text,
                expiration_date text
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
            insert into goods(goods_name,price,sales,manufacture_date,expiration_date) values('%s','%f','%d','%s','%s')
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
        data_list = self.cur.fetchall()
        output_list = []
        for item in data_list:
            output_dict = {
                "good_id": item[0],
                "goods_name": item[1],
                "price": item[2],
                "sales": item[3],
                "manufacture_date": item[4],
                "expiration_date": item[5]
            }
            output_list.append(output_dict)

        return output_list

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

    def deleteUser(self, _id):
        del_user_sql = """
            delete from users where id = '%d'
        """ % _id

        self.cur.execute(del_user_sql)
        self.common.commit()
        self.common.close()

    def deleteGoods(self, _id):
        del_goods_sql = """
            delete from goods where id = '%d'
        """ % _id
        self.cur.execute(del_goods_sql)
        self.common.commit()
        self.common.close()

    def updateUserPwd(self, _password, _id):
        update_user_sql = """
            update users set password = '%s' where id = '%d'
        """ % (_password, _id)

        self.cur.execute(update_user_sql)
        self.common.commit()
        self.common.close()

    def updateGoods(self, _price, _sales, _manufacture_date, _expiration_date, _id):
        update_goods_sql = """
            update goods set price = '%f',sales='%d',manufacture_date='%s', expiration_date='%s' where id = '%d'
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

    def selectGoodsOrderSales(self):
        select_goods_order_sales_sql = """
            select * from goods order by sales desc 
        """

        self.cur.execute(select_goods_order_sales_sql)
        data_list = self.cur.fetchall()
        output_list = []
        for item in data_list:
            output_dict = {
                "good_id": item[0],
                "goods_name": item[1],
                "price": item[2],
                "sales": item[3],
                "manufacture_date": item[4],
                "expiration_date": item[5]
            }

            output_list.append(output_dict)

        return output_list


if __name__ == '__main__':
    data_operate = dataBaseOperate("market.db")
    # data_operate.insertGoods("beef", 124.8, 12, "2024-10-24 18:00:00",
    #                          "2024-11-24 18:00:00")
    # print(data_operate.selectGoodsList())
    # data_operate.insertUser("string123", md5_encrypt("string"))
    # data_operate.deleteUser()
    # data_operate.common.commit()
    # users = data_operate.selectUserList()
    # user = data_operate.selectUserId("string123", md5_encrypt("string"))[0][0]
    # data_operate.common.close()

    # print(data_operate.selectGoodsOrderSales())
    data_operate.deleteGoods(3)
