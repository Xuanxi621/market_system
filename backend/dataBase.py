import sqlite3


class dataBase:
    def __init__(self, dbname):
        self.common = sqlite3.connect(dbname)
        self.cur = self.common.cursor()

    def userDataBase(self):
        create_user_sql = """
            create table if not exists users(
                id integer,
                name text,
                password text,
                role integer
            )
        """
        self.cur.execute(create_user_sql)


class dataBaseText(dataBase):
    def __init__(self, dbname):
        super().__init__(dbname)
        self.userDataBase()

    def insertUser(self):
        insert_user_sql = """
            insert into users values(1,"XiaoMing","123456",1)
        """

        self.cur.execute(insert_user_sql)

    def selectUser(self):
        select_user_sql = """
            select * from users
        """

        self.cur.execute(select_user_sql)
        return self.cur.fetchall()

    def deleteUser(self):
        del_user_sql = """
            delete from users where id = 1
        """

        self.cur.execute(del_user_sql)

    def updateUser(self):
        update_user_sql = """
            update users set name = "SSA",password = "123456",role = 0 where id =1
        """

        self.cur.execute(update_user_sql)


if __name__ == '__main__':
    data_text = dataBaseText("market.db")
    # data_text.insertUser()
    # data_text.deleteUser()
    # data_text.common.commit()
    users = data_text.selectUser()
    data_text.common.close()
    for user in users:
        print(user)
