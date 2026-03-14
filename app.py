from flask import Flask
from routes.routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config')

    app.register_blueprint(main_bp)
    return app
app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True, reloader_type='stat')