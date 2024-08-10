import sys

import requests


if len(sys.argv) == 2:
    try:
        sys1 = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")


try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()['bpi']['USD']['rate_float']
    print(response)

except requests.RequestException:
    sys.exit("RequestException")


print(f"${response * float(sys.argv[1]):,.4f}")