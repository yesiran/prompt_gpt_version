"""项目入口"""
from app import create_app

# 通过工厂函数创建应用实例
app = create_app()

if __name__ == "__main__":
    # debug模式下启动，生产环境应由WSGI服务器托管
    app.run(host="0.0.0.0", port=5000, debug=True)
