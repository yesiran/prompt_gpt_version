"""应用初始化模块"""
from flask import Flask
from app.config import get_config
from app.logger import init_logger
from app.database import db
from app.routes.prompt import prompt_bp


def create_app() -> Flask:
    """应用工厂函数，用于创建Flask实例"""
    app = Flask(__name__)

    # 加载配置
    config = get_config()
    app.config["SQLALCHEMY_DATABASE_URI"] = config.database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["LOG_LEVEL"] = config.log_level

    # 初始化日志
    init_logger(app)

    # 初始化数据库
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(prompt_bp)

    return app
