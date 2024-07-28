import json
import threading
from websocket import WebSocketApp
from app.models.alert import Alert
from app.models.user import User
from app.services.email_service import send_email
from app import db

def handle_socket_message(app, ws, message):
    with app.app_context():
        msg = json.loads(message)
        symbol = msg['s']
        price = float(msg['c'])
        
        print(f"Received price update: {symbol} at {price}")
        
        alerts = Alert.query.filter_by(cryptocurrency=symbol, status='created').all()
        for alert in alerts:
            if (alert.target_price >= price > 0) or (alert.target_price <= price > 0):
                print(f"Alert triggered: {alert.id} for {symbol} at {price}")
                alert.status = 'triggered'
                db.session.commit()
                user = User.query.get(alert.user_id)
                send_email(user, alert)

def on_open(ws):
    print("WebSocket connection opened")
    symbols = ["BTCUSDT", "ETHUSDT"]
    for symbol in symbols:
        params = {
            "method": "SUBSCRIBE",
            "params": [f"{symbol.lower()}@ticker"],
            "id": 1
        }
        ws.send(json.dumps(params))

def on_close(ws, close_status_code, close_msg):
    print("WebSocket connection closed")

def on_error(ws, error):
    print(f"WebSocket error occurred: {error}")

def start_websocket(app):
    def run_websocket():
        websocket_url = "wss://stream.binance.com:9443/ws"
        ws = WebSocketApp(websocket_url,
                          on_message=lambda ws, msg: handle_socket_message(app, ws, msg),
                          on_open=on_open,
                          on_close=on_close,
                          on_error=on_error)
        ws.run_forever()

    websocket_thread = threading.Thread(target=run_websocket)
    websocket_thread.daemon = True
    websocket_thread.start()