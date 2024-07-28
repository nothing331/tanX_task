from flask import Flask
from config import Config
from app.extensions import db, migrate, jwt, redis_client

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Import and register blueprints
    from app.routes import auth, alerts
    app.register_blueprint(auth.bp)
    app.register_blueprint(alerts.bp)

    # Start WebSocket in a background thread
    from app.services.price_service import start_websocket
    start_websocket(app)

    return app