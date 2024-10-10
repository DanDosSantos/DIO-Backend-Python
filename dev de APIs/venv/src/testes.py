from flask import Flask, url_for, request

app = Flask(__name__)

# @app.route("/")
# def hello_marte():
#     return "<h1>Hello, Mars!!!!</h1>"

@app.route('/hello')
def hello():
    return {"message": "Olá mundo!"}

@app.route('/eai/<usuario>/<int:idade>') #Passar os dados como argumento na url
def eai(usuario, idade):
    return {
        'Usuario': usuario,
        'Idade': idade
    }

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        return 'This is a GET'
    else:
        return 'This is POST'

with app.test_request_context():
    print(url_for('hello'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    print(url_for('eai', usuario='Daniel', idade=24))


app.run(debug=True)