# 导入相关扩展类库
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_moment import Moment
from flask_login import LoginManager
from flask_socketio import SocketIO

# 创建相关扩展对象
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
login_manager = LoginManager()



def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    # 会话保护
    # 默认：basic
    # 最高：strong
    # 不使用：None
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'user.login'
    login_manager.login_message = '需要登陆才可访问'
