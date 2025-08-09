"""Prompt相关的数据模型"""
from datetime import datetime
from app.database import db


class Prompt(db.Model):
    """存储Prompt基本信息"""
    __tablename__ = "prompts"

    id = db.Column(db.Integer, primary_key=True)
    # Prompt标题
    title = db.Column(db.String(255), nullable=False)
    # Prompt内容
    content = db.Column(db.Text, nullable=False)
    # 标签，使用逗号分隔多个标签
    tags = db.Column(db.String(255), nullable=True)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # 更新时间
    update_time = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # 与版本的关系，一个Prompt可以有多个版本
    versions = db.relationship("PromptVersion", backref="prompt", lazy=True)


class PromptVersion(db.Model):
    """Prompt版本记录"""
    __tablename__ = "prompt_versions"

    id = db.Column(db.Integer, primary_key=True)
    # 对应的Prompt ID
    prompt_id = db.Column(db.Integer, db.ForeignKey("prompts.id"), nullable=False)
    # 版本号，从1开始递增
    version = db.Column(db.Integer, nullable=False)
    # 版本内容
    content = db.Column(db.Text, nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # 更新时间
    update_time = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
