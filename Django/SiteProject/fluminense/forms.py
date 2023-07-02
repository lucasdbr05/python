from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from fluminense.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao = PasswordField('Confição da senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email= email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça o login para continuar.')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar foto de perfil.', validators=[FileAllowed(['jpg','png'])])

    curso_excel = BooleanField('Excel Impressionador')
    curso_vba = BooleanField('VBA  Impressionador')
    curso_python = BooleanField('Python  Impressionador')
    curso_powerbi = BooleanField('Power BI  Impressionador')
    curso_ppt = BooleanField('PowerPoint  Impressionador')
    curso_sql = BooleanField('SQL  Impressionador')

    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email= email.data).first()
            if usuario:
                raise ValidationError('Já há usuário com este e-mail cadastrado.')


class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo do Post', validators= [DataRequired(), Length(1,50)])
    corpo = TextAreaField('Escreva Aqui seu texto', validators=[DataRequired(), Length(0,500)])
    botao_submit = SubmitField('Criar Post')