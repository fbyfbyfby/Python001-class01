import pymysql


dbInfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'rootroot',
    'db': 'test'
}

sqls = ["INSERT INTO week2_test (name, genra, release_date) VALUES (%s, %s, %s)"]


class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls
        self.result = []
 

    def run(self, obj_insert: tuple):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
 
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command, obj_insert)
 
            cur.close()
            conn.commit()
        except:
            conn.rollback()
 
        conn.close()

if __name__ == "__main__":
    db = ConnDB(dbInfo, sqls)
    db.run()
    print(db.result)
