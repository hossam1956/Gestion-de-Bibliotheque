import mysql.connector as mc
import hashlib
class Connexion:
    def __init__(self):
        self.host="localhost"
        self.database="user"
        self.user="root"
        self.password=""
        self.port=3306
        self.conn = None
        self.cursor = None
        self.table = "adherent"

    def connect(self):
        try:
            self.conn = mc.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            print("connect to database")
        except mc.Error as err:
            print(err)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close
        if self.conn:
            self.conn.close

    def getAll(self):
        req = f"select * from {self.table}"
        self.cursor.execute(req)
        tasks = self.cursor.fetchall()
        return tasks

    def add(self, username,password):
        req = f"insert into {self.table}(username,password,admin)values(%s,md5(%s),0)"
        values = (username,password,)
        self.cursor.execute(req, values)
        self.conn.commit()

    def update(self, username,password,id):
        req = f"update {self.table} set username=%s , password=md5(%s) where id=%s"
        values = (username,password,id)
        self.cursor.execute(req, values)
        self.conn.commit()

    def delete(self, id):
        req = f"delete from {self.table} where id=%s"
        values = (id,)
        self.cursor.execute(req, values)
        self.conn.commit()
    def verify(self,usr,pwd):
        adm=0
        hash_object = hashlib.md5(pwd.encode())
        md5_hash = hash_object.hexdigest()
        text=md5_hash[:20]
        req = f"SELECT * FROM {self.table} WHERE username = %s AND password = %s"
        req1 = f"SELECT * FROM {self.table} WHERE username = %s AND password = %s AND admin=1"
        values = (usr, text)
        self.cursor.execute(req, values)
        res = self.cursor.fetchone()
        self.cursor.execute(req1, values)
        adm=self.cursor.fetchone()
        if res is not None:
            if adm is not None:
                return 2
            else:
                return 1
        else:
            return 0





