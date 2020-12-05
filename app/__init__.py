from flask import Flask, render_template
# 导入配置
from app.config import config
# 导入第三方扩展配置
from app.extensions import config_extensions
# 导入蓝本
from app.views import config_blueprint


def create_app(config_name):
    # 创建应用实例
    app = Flask(__name__)
    # 通过类初始化配置
    app.config.from_object(config[config_name])
    # 调用初始化函数
    config[config_name].init_app(app)
    # 配置相关扩展
    config_extensions(app)
    # 配置相关蓝本
    config_blueprint(app)
    # 配置错误显示
    config_errorhandler(app)
    # 返回应用实例
    return app


def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html')
