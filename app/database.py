"""数据库模块，封装SQLAlchemy初始化"""
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy实例，全局共享
# SQLAlchemy是一个ORM框架，用于在Python对象和数据库之间建立映射
# 使用它可以通过操作对象来读写数据库，而无需编写SQL语句

db = SQLAlchemy()
