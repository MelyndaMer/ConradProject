from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length



class FormularioRegistro(FlaskForm):
    name = StringField('Nombre completo', validators=[DataRequired(), Length(max=64)])
    tel = StringField('Teléfono de contacto', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirmar_password = PasswordField('Confirmar contraseña', validators=[DataRequired()])  
    date = DateField('Fecha de nacimiento', validators=[DataRequired()])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')



class FormularioLogin(FlaskForm):
    email = StringField('Correo', validators=[DataRequired()])
    password = PasswordField('Cotraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')