from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes.prompts import bp as prompts_bp
    from .routes.ui import ui_bp

    app.register_blueprint(prompts_bp)
    app.register_blueprint(ui_bp)

    return app
