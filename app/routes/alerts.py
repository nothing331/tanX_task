from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.alert import Alert
from app import db, redis_client
from app.services.email_service import send_email
import json
from datetime import timedelta

bp = Blueprint('alerts', __name__, url_prefix='/alerts')

@bp.route('/create/', methods=['POST'])
@jwt_required()
def create_alert():
    data = request.json
    user_id = get_jwt_identity()
    new_alert = Alert(
        user_id=user_id,
        cryptocurrency=data['cryptocurrency'],
        target_price=data['target_price']
    )
    db.session.add(new_alert)
    db.session.commit()
    return jsonify({"message": "Alert created successfully", "alert_id": new_alert.id}), 201

@bp.route('/delete/<int:alert_id>', methods=['DELETE'])
@jwt_required()
def delete_alert(alert_id):
    user_id = get_jwt_identity()
    alert = Alert.query.filter_by(id=alert_id, user_id=user_id).first()
    if alert:
        db.session.delete(alert)
        db.session.commit()
        return jsonify({"message": "Alert deleted successfully"}), 200
    return jsonify({"message": "Alert not found"}), 404


@bp.route('/', methods=['GET'])
@jwt_required()
def get_alerts():
    user_id = get_jwt_identity()
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    status_filter = request.args.get('status')

    cache_key = f"user:{user_id}:alerts:page:{page}:status:{status_filter}"
    
    # Check if Redis is available
    if redis_client is not None:
        cached_data = redis_client.get(cache_key)
        if cached_data:
            return json.loads(cached_data)

    # Your existing database query logic here
    query = Alert.query.filter_by(user_id=user_id)
    if status_filter:
        query = query.filter_by(status=status_filter)

    pagination = query.paginate(page=page, per_page=per_page)
    alerts = [{
        "id": alert.id,
        "cryptocurrency": alert.cryptocurrency,
        "target_price": alert.target_price,
        "status": alert.status,
        "created_at": alert.created_at.isoformat()
    } for alert in pagination.items]

    result = {
        "alerts": alerts,
        "total_pages": pagination.pages,
        "current_page": page
    }

    # Cache the result if Redis is available
    if redis_client is not None:
        redis_client.setex(cache_key, timedelta(minutes=5), json.dumps(result))

    return jsonify(result), 200