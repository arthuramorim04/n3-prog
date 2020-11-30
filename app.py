from flask import Flask, request, json
from resources import Routes

app = Flask(__name__)

routes = Routes()


@app.route('/')
def hello_world():
    return 'Hello World!'


# Modelo do JSON
# Create
# {
#     "matricula": 5,
# 	  "nome": "teste123",
#     "email": "teste123@gmail.com",
#     "turma" : "ADS41",
#     "dataMatricula": "10/02/2020"
# }
#
# FindOne e Delete
# {
#     "matricula": 2
# }
@app.route('/create', methods=['POST'])
def createUser():
    response = routes.create(request)
    return response


@app.route('/delete', methods=['DELETE'])
def deleteUser():
    return routes.remove(request)


@app.route('/findOne', methods=['GET'])
def findOne():
    response = routes.findOne(request)
    return response


@app.route('/findAll', methods=['GET'])
def findAll():
    response = routes.findAll()
    return response


if __name__ == '__main__':
    app.run()
    use_debugger = True
    app.run(use_debugger=use_debugger, debug=app.debug,
            use_reloader=use_debugger, host='0.0.0.0')
