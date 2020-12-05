import os


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")

    # 进行拼接
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


# 通用配置
class Config:
    # DEBUG 默认为 False
    DEBUG = False

    # TESTING 默认为 False
    TESTING = False
    # 秘钥
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or r"M*\x92\x16\x01\x17:\xc4'\xab \x06\xe7\x1d*\xaa\xc1s\xb8\x88\xfb\xb7\x15\xcd"
    # 数据库操作
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 邮件配置
    # 服务器ip地址
    MAIL_SERVER = "smtp.qq.com"
    # 端口号:TLS对应587,SSL对应465
    MAIL_PORT = "587"
    MAIL_USE_TLS = True
    # MAIL_USE_SSL : 默认为 False
    # 发送者邮箱
    MAIL_USERNAME = "dalongmao.zhang@qq.com"
    # 发送者QQ邮箱授权码(进入邮箱发送短信申请即可，具体参照下图)
    MAIL_PASSWORD = "ohhvvhwltfovbgac"
    # 默认发送者
    MAIL_DEFAULT_SENDER = "dalongmao.zhang@qq.com"

    # 初始化的方法
    @staticmethod
    def init_app(app):
        pass


# 开发环境配置
class DevelopmentConfig(Config):
    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "872039610",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flask_end"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


# 测试环境配置
class TestingConfig(Config):
    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "872039610",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flask_end"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


# 生产环境配置
class ProductionConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "872039610",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flask_end"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


# 配置字典
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    # 默认配置
    'default': DevelopmentConfig
}
