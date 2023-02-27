from load_keys import keys
from binance.spot import Spot

if __name__ == "__main__":

    secret_key = keys['secret_key']
    api_key = keys['api_key']

    client = Spot(base_url='https://testnet.binance.vision')
    print(client.time())

    client = Spot(api_key=api_key, api_secret=secret_key)

    print(client.account())

    # Post a new order
    params = {
        'symbol': 'BNBUSDT',
        'side': 'SELL',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': 0.1,
        'price': 350
    }

    response = client.new_order_test(**params)

    print(response)
