from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abscnaskucgkugaxkubanxkaukxdvsbfsyukvabsxkaguybxaw'

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/users/<user>")
def users(user):
    return render_template('usuarios.html',user=user)

@app.route('/<string:nome>')
def error(nome):
    return f'<h1>Pagina "{nome}" não existe</h1>'

if __name__ == "__main__":
    app.run(debug= True)