import re
import json
from rpc_class import coinrpc
from restful_lib import Connection
from bitcoinrpc.authproxy import AuthServiceProxy

# get bitcoin rpc config
bitcoinrpc = coinrpc("../../bitcoin-0.10.2/bitcoin/bitcoin.conf").rpccon()

# get litecoin rpc config
litecoinrpc = coinrpc("../../litcoin-xxx/bitcoin/bitcoin.conf").rpccon()

# make a new bitcoin address to receive the shifted funds
newaddress = bitcoinrpc.getnewaddress()

# connect to shapeshift API
base_url = "https://shapeshift.io"
conn = Connection(base_url)

# change litecoin to bitcoin
post_data = {"withdrawal":newaddress, "pair":"ltc_btc"}
btc_shift = conn.request_post("/shift/", post_data)

for item in btc_shift:
    if item == "body":
        response = json.loads(btc_shift[item])

for key, value in response.iteritems():
    if key == "deposit":
        depositaddr = value

# send to deposit address
litecoinrpc.sendtoaddress(depositaddr, 10)
