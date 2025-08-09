"""日志模块，提供统一的日志配置"""
import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

# 日志文件存放目录
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def init_logger(app) -> None:
    """初始化日志配置

    参数:
        app: Flask应用实例
    """
    log_level = app.config.get("LOG_LEVEL", "DEBUG")

    # 创建主日志处理器，按日期切分日志文件
    file_handler = TimedRotatingFileHandler(
        filename=LOG_DIR / "prompt_project_log.log",
        when="midnight",
        interval=1,
        encoding="utf-8",
        backupCount=7,
    )
    file_handler.setLevel(log_level)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    # 错误日志单独处理器
    error_handler = TimedRotatingFileHandler(
        filename=LOG_DIR / "prompt_project_error.log",
        when="midnight",
        interval=1,
        encoding="utf-8",
        backupCount=7,
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    # 将处理器添加到应用的logger
    app.logger.addHandler(file_handler)
    app.logger.addHandler(error_handler)
    app.logger.setLevel(log_level)
