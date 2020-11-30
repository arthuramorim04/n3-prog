from pymongo import MongoClient


class MongoConnect():

    def connectionAlunos(self):
        client = MongoClient('localhost', 27017)
        banco = client['n3']
        alunos = banco['alunos']
        return alunos

    def insert(self, obj):
        try:
            MongoConnect().connectionAlunos().insert_one(obj).inserted_id

        except Exception as e:
            print(obj)
            print(e)

    def delete(self, matricula):
        try:
            return MongoConnect.connectionAlunos().delete_one({"matricula": matricula})
        except Exception as e:
            print("--------//------")
            print(e)

    def findOne(self,matricula):
        try:
            return MongoConnect().connectionAlunos().find_one({"matricula": matricula})
        except Exception as e:
            print("--------//------")
            print(e)

    def findAll(self):
        try:
            return MongoConnect().connectionAlunos().find()
        except Exception as e:
            print("--------//------")
            print(e)