import websocket
import json
import sqlite3
from datetime import datetime

# ---------------------------
# Create SQLite database
# ---------------------------
conn = sqlite3.connect('data/stock_data.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS stock_prices (
    id INTEGER PRIMARY KEY,
    ticker TEXT,
    timestamp DATETIME,
    price REAL
)
''')
conn.commit()

# ---------------------------
# Define WebSocket behaviour
# ---------------------------
def on_message(ws, message):
    """
    Called when a new message is received from Yahoo Finance WebSocket.
    """
    try:
        data = json.loads(message)
        # Only handle quote updates
        if 'quote' in data:
            quote = data['quote']
            ticker = quote['s']         # Symbol
            price = quote['p']          # Last price
            timestamp = datetime.now()

            # Insert into database
            c.execute('INSERT INTO stock_prices (ticker, timestamp, price) VALUES (?, ?, ?)',
                      (ticker, timestamp, price))
            conn.commit()

            print(f"{timestamp} | {ticker}: ${price}")

    except Exception as e:
        print("Error parsing message:", e)

def on_error(ws, error):
    print("WebSocket error:", error)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")
    conn.close()

def on_open(ws):
    """
    Subscribe to a ticker(s). For example, Apple (AAPL).
    The subscription message format is based on Yahoo Finance WebSocket observed messages.
    """
    tickers = ["AAPL"]  # Add more tickers if you like
    for ticker in tickers:
        subscribe_msg = {
            "subscribe": [ticker]
        }
        ws.send(json.dumps(subscribe_msg))
        print(f"Subscribed to {ticker}")

# ---------------------------
# Connect to WebSocket
# ---------------------------
url = "wss://streamer.finance.yahoo.com"  # Yahoo Finance WebSocket URL

ws = websocket.WebSocketApp(
    url,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

print("Connecting to Yahoo Finance WebSocket...")
ws.run_forever()
