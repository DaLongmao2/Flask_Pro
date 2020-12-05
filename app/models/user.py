# coding = utf-8
from datetime import datetime

from flask import current_app

from app.extensions import db, login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# 创建用户类
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(38), unique=True)
    password_hash = db.Column(db.String(288), nullable=True)
    email = db.Column(db.String(64), nullable=True)
    activation = db.Column(db.Boolean, default=False)

    # 保护字段
    @property
    def password(self):
        raise AttributeError('密码属性不可读')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # TODO：这里是生成激活的token
    def generate_activate_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': self.id})

    # TODO: 激活账户时的token校验，校验时还不知道用户信息，需要静态方法
    # 静态方法 就和普通函数一样 但是写在类的里面
    @staticmethod
    def check_activate_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        user = User.query.get(data.get('id'))
        if user is None:
            # 不存在此用户
            return False
        if not user.activation:
            # 账户没有激活时才激活
            user.activation = True
            db.session.add(user)
        return True


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))


# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     content = db.Column(db.Text, nullable=False)
#     create_time = db.Column(db.DateTime, default=datetime.now(), index=True)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     author = db.relationship('User', back_populates='messages')
# 不重要
# def loader_user2(user_id):
#     return User.query.get(int(user_id))

