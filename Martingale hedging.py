import requests
import time
import hmac
import hashlib

# HashKey API credentials and endpoint
hashkey_api_key = 'YOUR_HASHKEY_API_KEY'
hashkey_secret_key = 'YOUR_HASHKEY_SECRET_KEY'
hashkey_base_url = 'https://api.hashkey.com'

# Get HashKey futures market price
def get_hashkey_futures_price(symbol):
    endpoint = f'/api/v1/futures/market/ticker?symbol={symbol}'
    url = hashkey_base_url + endpoint
    response = requests.get(url)
    return float(response.json()['price'])

# Sign request (needed for authenticated endpoints)
def sign_request(params, secret_key):
    query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
    signature = hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    return signature

# Place an order on HashKey
def send_hashkey_futures_order(symbol, side, quantity, price, leverage=1, order_type='LIMIT'):
    endpoint = '/api/v1/futures/order'
    url = hashkey_base_url + endpoint
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'side': side,  # BUY or SELL
        'type': order_type,
        'price': price,
        'quantity': quantity,
        'leverage': leverage,
        'timestamp': timestamp,
        'recvWindow': 5000,
        'apiKey': hashkey_api_key
    }
    params['sign'] = sign_request(params, hashkey_secret_key)
    response = requests.post(url, data=params)
    return response.json()

# Martingale with Hedge Trading Strategy
def martingale_with_hedge_strategy():
    symbol = 'BTCUSDT'
    initial_trade_size = 0.001  # Initial trade size
    leverage = 5  # Leverage for futures trading
    price_threshold = 100.0  # Price movement threshold to trigger a new trade
    max_trades = 5  # Maximum number of trades in the Martingale sequence
    hedge_side = 'SELL'  # Side for hedging (opposite of initial trade)
    
    # Get the initial market price
    entry_price = get_hashkey_futures_price(symbol)
    trade_size = initial_trade_size
    current_trade_count = 0

    while current_trade_count < max_trades:
        # Place initial trade
        response = send_hashkey_futures_order(symbol, 'BUY', trade_size, entry_price, leverage)
        print(f"Placed initial BUY order: {response}")
        
        # Monitor the market for price movements
        while True:
            current_price = get_hashkey_futures_price(symbol)
            
            # Check if price has moved beyond the threshold
            if current_price <= entry_price - price_threshold:
                current_trade_count += 1
                trade_size *= 2  # Double the trade size for Martingale
                
                # Place a new BUY order at the current price
                response = send_hashkey_futures_order(symbol, 'BUY', trade_size, current_price, leverage)
                print(f"Placed additional BUY order: {response}")
                
                # Place a hedge SELL order at the current price to limit risk
                hedge_response = send_hashkey_futures_order(symbol, hedge_side, trade_size, current_price, leverage)
                print(f"Placed hedge SELL order: {hedge_response}")
                
                # Update entry price for the next round
                entry_price = current_price
                break

            # Sleep before checking the price again
            time.sleep(60)

        # Check if max trades reached
        if current_trade_count >= max_trades:
            print("Maximum trades reached. Stopping strategy.")
            break

# Start the strategy
if __name__ == "__main__":
    martingale_with_hedge_strategy()
