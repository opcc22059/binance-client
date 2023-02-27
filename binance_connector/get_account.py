import sys
from pathlib import Path

base_path = str(Path(__file__).resolve().parent.parent)
print('current path: ', base_path)

sys.path.append(base_path)
print('path: ', sys.path)

from utils.load_keys import keys
from binance.spot import Spot

if __name__ == "__main__":

    secret_key = keys['secret_key']
    api_key = keys['api_key']

    client = Spot(
        # base_url='https://testnet.binance.vision',
        api_key=api_key, 
        api_secret=secret_key
    )
    print(client.time())

    response = client.account()
    balances = response['balances']
    for asset in balances:
        if asset['asset'] == 'USDT':
            print(asset)
