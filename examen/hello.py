from flask import Flask,redirect
from flask import render_template
from flask import request
from markupsafe import escape

from final import palabras_mas_repetidas
app = Flask(__name__)



@app.route('/', methods=['POST','GET'])
def calcular():
    if request.method == 'POST':
        oracion = request.form.get('dato')

        salida = palabras_mas_repetidas(oracion)
       
        return render_template('index.html',salida=salida,dato=oracion)   
        
    else:
        return render_template('index.html')