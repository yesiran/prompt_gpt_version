# prompt_gpt_version

用于管理Prompt的轻量级平台，基于Flask和MySQL实现。

## 开发环境
- Python 3.11
- Flask 3
- MySQL 8

## 快速开始
1. 复制`.env.template`为`.env`并填写数据库等配置。
2. 安装依赖：`pip install -r requirements.txt`
3. 初始化数据库（示例）：
   ```python
   from app import create_app
   from app.database import db
   app = create_app()
   with app.app_context():
       db.create_all()
   ```
4. 运行项目：`python run.py`

项目目前仅实现基础的Prompt增删改查及版本记录，后续会逐步迭代完善。
