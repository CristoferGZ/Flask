from flask import Flask, render_template  # agregado render_template!
app = Flask(__name__)                     
    
"""
@app.route('/k')
def colocolito():
    return render_template('corro-corro.html')


@app.route('/')
def indeex():
    return render_template("index.html", frase="hola", times=5)	# ¡Fíjate en los 2 nuevos argumentos nombrados!


@app.route('/play')
def indexx():
    return render_template("cuairo.html", frase="hola", times=5)

"""


@app.route('/lists')
def render_lists():
    estudiantes_info = [
        {'name' : 'Michael', 'edad' : 35},
        {'name' : 'John', 'edad' : 30 }, 
        {'name' : 'Mark', 'edad' : 25},
        {'name' : 'KB', 'edad' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], student = estudiantes_info)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ajedrez.html', row=8, col=8, color_1="red", color_2="black") 

@app.route('/<int:fila>')
def fila(fila):
    return render_template('ajedrez.html', row=fila, col=8, color_1="red", color_2="black")                    

@app.route('/<int:fila>/<int:columna>')
def fila_columna(fila,columna):
    return render_template('ajedrez.html', row=fila, col=columna, color_1="red", color_2="black")         

@app.route('/<int:fila>/<int:columna>/<string:color_1>/<string:color_2>')
def fila_columna_color(fila,columna,color_1,color_2):
    return render_template('ajedrez.html', row=fila, col=columna, color_1=color_1, color_2=color_2)         

if __name__== "__main__":
    app.run(debug=True)                   

