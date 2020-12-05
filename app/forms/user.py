# coding = utf-8
# 导入基类
from flask_wtf import FlaskForm
# 导入相关字段 文本 密码 提交
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
# 导入相关验证 邮箱 相等 所需数据 长度
from wtforms.validators import Email, EqualTo, DataRequired, Length
from app.models import User


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(2, 28, message='用户名必须在2-28位')])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 28, message='密码必须在6-28位')])
    password_equalto = PasswordField('确认密码', validators=[DataRequired(), EqualTo('password', message='两次密码不正确')])
    email = StringField('邮箱', validators=[DataRequired(), Email(message='请输入正确的邮箱格式')])
    submit = SubmitField('提交')

    # 自定义验证器，验证用户名
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已存在，请选用其它用户名')

    # 自定义验证器，验证邮箱
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已使用，请选用其它邮箱')


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    Remember_password = BooleanField('记住密码')
    submit = SubmitField("登陆")

    def validate_username(self, field):
        if not User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名不存在,请重新输入')
