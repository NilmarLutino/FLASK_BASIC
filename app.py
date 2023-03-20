from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/saludo')
def index():
    return '¡Hola, mundo!'

@app.route('/saludo/<nombre>')
def saludo(nombre):
    try:
        return render_template('saludo.html', nombre=nombre)
    except Exception as e:
        print(e)
        return "Ha ocurrido un error: " + str(e)



if __name__ == '__main__':
    app.run(debug = True)
    app.run()
