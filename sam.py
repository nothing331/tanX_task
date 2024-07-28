import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    price = float(data['p'])
    print(f"Current BTC price: {price}")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send(json.dumps({"method": "SUBSCRIBE", "params": ["btcusdt@trade"], "id": 1}))

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws",
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
