from wtforms import Form, StringField, PasswordField, SubmitField, validators


class RegistrationForm(Form):
    username = StringField("Username",
                           [validators.DataRequired(),
                            validators.Length(min=2, max=20)])
    email = StringField('Email',
                        [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password',
                             [validators.DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     [validators.DataRequired(),
                                      validators.EqualTo('password')])
    submit = SubmitField('Submit')


class LoginForm(Form):
    email = StringField('Email',
                        [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password',
                             [validators.DataRequired()])
    submit = SubmitField('Register')
