from flask import json
import json
from bson import ObjectId
from storage.connection import MongoConnect

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class Aluno():

    def insert(self, aluno):
        con = MongoConnect()
        model = {
            "matricula": aluno['matricula'],
            "nome": aluno['nome'],
            "email": aluno['email'],
            "turma": aluno['turma'],
            "dataMatricula": aluno['dataMatricula']
        }
        try:
            con.insert(model)
            return JSONEncoder().encode(model), 200
        except:
            return JSONEncoder().encode(model), 404

    def delete(self, matricula):
        con = MongoConnect()
        try:
            con.delete(matricula)
            return JSONEncoder().encode("Aluno deletada pela matricula"), 200
        except:
            return JSONEncoder().encode("Nao encontramos esse aluno"), 404

    def findOne(self, matricula):
        con = MongoConnect()
        try:
            result = con.findOne(matricula)
            print(result)
            if result == None:
                return JSONEncoder().encode("Nao encontramos esse aluno"), 404
            return JSONEncoder().encode(result), 200
        except:
            return JSONEncoder().encode("No have registers"), 404

    def findAll(self):
        con = MongoConnect()
        try:
            listAlunos = []
            for aluno in con.findAll():
                listAlunos.append(aluno)
            print(listAlunos)
            return JSONEncoder().encode(listAlunos), 200
        except Exception as e:
            print(e)
            return "error", 404