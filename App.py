from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


@app.route('/procesar_ejercicio1', methods=['POST'])
def procesar_ejercicio1():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    cantidad_tarros = int(request.form['cantidad'])
    
  
    precio_tarro = 9000
    total_sin_descuento = cantidad_tarros * precio_tarro
    
    
    if 18 <= edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25
    else:
        descuento = 0
    
    descuento_aplicado = total_sin_descuento * descuento
    total_con_descuento = total_sin_descuento - descuento_aplicado
    
    return render_template('resultado1.html', 
                         nombre=nombre,
                         total_sin_descuento=total_sin_descuento,
                         descuento=descuento * 100,
                         total_con_descuento=total_con_descuento)


@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')


@app.route('/procesar_ejercicio2', methods=['POST'])
def procesar_ejercicio2():
    usuario = request.form['usuario']
    contraseña = request.form['contraseña']
    
   
    usuarios = {
        'juan': {'contraseña': 'admin', 'tipo': 'administrador'},
        'pepe': {'contraseña': 'user', 'tipo': 'usuario'}
    }
    
    mensaje = ""
    
    if usuario in usuarios and usuarios[usuario]['contraseña'] == contraseña:
        tipo_usuario = usuarios[usuario]['tipo']
        mensaje = f"Bienvenido {tipo_usuario} {usuario}"
    else:
        mensaje = "Usuario o contraseña incorrectos"
    
    return render_template('resultado2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)