import requests


my_exchange_code = input("> ").lower()
resp = dict(requests.get(f"http://www.floatrates.com/daily/{my_exchange_code}.json").json())
if my_exchange_code == 'usd':
    currency = {
        'usd': resp['eur']['inverseRate'],
        'eur': resp['eur']['rate']
    }
elif my_exchange_code == 'eur':
    currency = {
        'usd': resp['usd']['rate'],
        'eur': resp['usd']['inverseRate']
    }
else:
    currency = {
        'usd': resp['usd']['rate'],
        'eur': resp['eur']['rate']
    }

while currency_exchange_code := input("> ").lower():
    count = float(input("> "))
    print("Checking the cache...")
    if currency_exchange_code in currency.keys():
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        currency.update({currency_exchange_code: resp[currency_exchange_code.lower()]['rate']})
    print(f"You received {round(currency[currency_exchange_code] * count, 2)} {currency_exchange_code.upper()}.")
