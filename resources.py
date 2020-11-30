from flask import Flask, request, json
from services.Alunos import Aluno

controller = Aluno()

class Routes:
    def create(self, req):
        aluno = req.get_json()
        ifPresent = controller.findOne(aluno['matricula'])
        if aluno['nome'] == "":
            return json.dumps({"code": 400, "description": "o nome deve estar preenchido", }), 400
        elif len(aluno['turma']) > 100:
            return json.dumps({"code": 400,
                               "description": "voê deve registrar o aluno em uma turma", }), 400
        elif aluno['dataMatricula'] == "":
            return json.dumps({"code": 400, "description": "você deve informar a data da matricula", }), 400
        elif aluno['email'] == "":
            return json.dumps({"code": 400, "description": "e-mail invalido", }), 400
        elif len(aluno['email']) > 400:
            return json.dumps(
                {"code": 400, "description": "e-mail deve conter menos de 400 caracteres incluindo seu dominio", }), 400
        response = controller.insert(aluno)
        return response

    def remove(self, req):
        aluno = req.get_json()
        matricula = aluno['matricula']
        alunoCadastrado = controller.findOne(matricula)
        if alunoCadastrado == None:
            return json.dumps(
                {"code": 400, "description": "matricula do aluno não encontrada", }), 400
        response = controller.delete(matricula)
        return response

    def findOne(self,req):
        aluno = req.get_json()
        matricula = aluno['matricula']
        response = controller.findOne(matricula)
        return response

    def findAll(self):
        response = controller.findAll()
        return response