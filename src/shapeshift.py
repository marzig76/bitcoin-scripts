import json
from restful_lib import Connection

# connect to shapeshift
base_url = "https://shapeshift.io"
conn = Connection(base_url)

# checking exchange rate
btc_ltc_rate = conn.request("/rate/btc_ltc")

for item in btc_ltc_rate:
    if item == "body":
        response = json.loads(btc_ltc_rate[item])

for key, value in response.iteritems():
    print key, value
