from conn import *
c=Connexion()
class Adherent:
    def __init__(self,username,password):
        self.username=username
        self.password = password
    def connect(self):
        c.connect()
    def insert(self):
        c.add(self.username,self.password)
    def update(self,id):
        c.update(self.username,self.password,id)
    def delete(self,id):
        c.delete(self,id)
    def getAll(self):
        c.getAll()
    def disconnect(self):
        c.disconnect()
    def verify(self,user,pwd):
        a=c.verify(user,pwd)
        if a==1:
            return 1
        elif a==2:
            return 2
        else:
            return 0
