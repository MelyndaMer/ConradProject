from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/inicio",methods=['GET', 'POST'])
def inicio():
    return render_template('index.html')

@app.route("/inicio/busqueda")
def busqueda():
    return render_template('reservar.html')

@app.route("/inicio/busqueda/reserva")
def reserva():
    return render_template('habitacion.html')

@app.route("/registro", methods=['GET', 'POST'])
def registro():
    return "<h1>rottenR<h1>"

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route("/inicio/perfil")
def perfil():
    return "<h1>rottenP<h1>"

@app.route("/inicio/perfil/admindashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True)