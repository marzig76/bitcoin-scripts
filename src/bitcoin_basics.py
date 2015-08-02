import re
from bitcoinrpc.authproxy import AuthServiceProxy

# get rpc config
conffile = open("../../bitcoin-0.10.2/bitcoin/bitcoin.conf")

for lines in conffile:
    line = re.split("=", lines)
    if line[0] == "rpcuser":
        rpcuser = line[1].strip()
    if line[0] == "rpcpassword":
        rpcpass = line[1].strip()

# create RPC connection
rpcconnection = "http://" + rpcuser + ":" + rpcpass + "@127.0.0.1:8332"
bitcoin_rpc = AuthServiceProxy(rpcconnection)

# just some basic functionality
#getinfostring = bitcoin_rpc.getinfo()
#getbalancestring = bitcoin_rpc.getbalance()
#getaddressesbyaccount = bitcoin_rpc.getaddressesbyaccount("")

# loop through all addresses in my wallet
#for address in bitcoin_rpc.getaddressesbyaccount(""):
#    print address
#print

# list addresses with known received amounts
for transactions in bitcoin_rpc.listreceivedbyaddress():
    for name in transactions:
        if name == "address":
            address = transactions[name]
        if name == "amount":
            amount = transactions[name]
    print "Address", address, "has recevied", amount, "bitcoin"

print

# make a new address
#newaddress = bitcoin_rpc.getnewaddress()

# send to new address
#bitcoin_rpc.sendtoaddress(newaddress, .001)
