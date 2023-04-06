from flask_wtf import FlaskForm
from wtforms import StringField,\
PasswordField, SubmitField, BooleanField
from wtforms.validators import\
DataRequired

class LoginForm(FlaskForm):
    username = StringField("User", validators=[DataRequired()], id="username")
    email = StringField("Email", validators=[DataRequired()], id="email")
    password = PasswordField("Password", validators=[DataRequired()], id="password")
    #rememberme = BooleanField("Remember me")
    submit = SubmitField("Submit")