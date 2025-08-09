"""应用配置模块，负责加载环境变量"""
from dataclasses import dataclass
from dotenv import load_dotenv
import os

# 在模块导入时加载.env文件
load_dotenv()

@dataclass
class Config:
    """配置对象，用于统一管理全局配置"""
    # Flask运行环境，例如development或production
    flask_env: str = os.getenv("FLASK_ENV", "development")
    # 数据库连接URL，使用MySQL作为存储
    database_url: str = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://username:password@localhost:3306/prompt_db",
    )
    # 日志级别，控制输出的详细程度
    log_level: str = os.getenv("LOG_LEVEL", "DEBUG")

def get_config() -> Config:
    """获取配置对象的工厂函数"""
    return Config()
