import re
import json
from restful_lib import Connection
from bitcoinrpc.authproxy import AuthServiceProxy

# get bitcoin rpc config
conffile = open("../../bitcoin-0.10.2/bitcoin/bitcoin.conf")

for lines in conffile:
    line = re.split("=", lines)
    if line[0] == "rpcuser":
        rpcuser = line[1].strip()
    if line[0] == "rpcpassword":
        rpcpass = line[1].strip()

# create RPC connection
bitcoinrpcconnection = "http://" + rpcuser + ":" + rpcpass + "@127.0.0.1:8332"
bitcoin_rpc = AuthServiceProxy(bitcoinrpcconnection)

# get litecoin rpc config
conffile = open("~/.litecoin/.bitcoin.conf")

for lines in conffile:
    line = re.split("=", lines)
    if line[0] == "rpcuser":
        rpcuser = line[1].strip()
    if line[0] == "rpcpassword":
        rpcpass = line[1].strip()

# create RPC connection
litecoinrpcconnection = "http://" + rpcuser + ":" + rpcpass + "@127.0.0.1:8332"
litecoin_rpc = AuthServiceProxy(litecoinrpcconnection)

# make a new bitcoin address to receive the shifted funds
newaddress = bitcoin_rpc.getnewaddress()

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
    if key = "deposit":
        depositaddr = value

# send to deposit address
litecoin_rpc.sendtoaddress(depositaddr, 10)
