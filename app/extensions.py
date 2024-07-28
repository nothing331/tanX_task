# app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import redis
from config import Config
import redis
from redis.exceptions import ConnectionError


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
# redis_client = redis.StrictRedis.from_url(Config.REDIS_URL)
try:
    redis_client = redis.StrictRedis.from_url(Config.REDIS_URL, decode_responses=True)
    redis_client.ping()  # Test the connection
except ConnectionError:
    print("Warning: Unable to connect to Redis. Caching will be disabled.")
    redis_client = None