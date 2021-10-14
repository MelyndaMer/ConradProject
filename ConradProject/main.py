from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import FormularioLogin, FormularioRegistro
from flask_login import LoginManager, current_user, login_user, logout_user
import flask_login
from modelos import usuarios, Usuario, get_usuario
from werkzeug.urls import url_parse


app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'



login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(id_usuario):
    for usuario in usuarios:
        if usuario.id == int(id_usuario):
            return usuario
    return None


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


@app.route("/inicio/perfil")
def perfil():
    return "<h1>rottenP<h1>"

@app.route("/inicio/perfil/admindashboard", methods=['GET', 'POST'])
def dashboard():
    usurisdct = {"Giacomo Guilizzoni":"10/10/2021","Marco Bottom":"11/5/2021","gggg":"7/6/2021","sss":"9/4/2021"}
    return render_template('dashboard.html', num = usurisdct)






@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = FormularioLogin()
    if form.validate_on_submit():
        user = get_usuario(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = FormularioRegistro()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Creación y guardado de usuario
        usuario = Usuario(len(usuarios) + 1, name, email, password)
        usuarios.append(usuarios)
        # Dejamos al usuario logueado
        login_user(usuario, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("registro.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)