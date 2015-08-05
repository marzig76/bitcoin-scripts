import re
import json
from restful_lib import Connection
from bitcoinrpc.authproxy import AuthServiceProxy

class coinrpc:

    rpcuser = ""
    rpcpass = ""

    def __init__(self, configfile):
        # get bitcoin rpc config
        conffile = open(configfile)

        for lines in conffile:
            line = re.split("=", lines)
            if line[0] == "rpcuser":
                self.rpcuser = line[1].strip()
            if line[0] == "rpcpassword":
                self.rpcpass = line[1].strip()

    def rpccon(self):
        rpcconnection = "http://" + self.rpcuser + ":" + self.rpcpass + "@127.0.0.1:8332"
        rpc = AuthServiceProxy(rpcconnection)
        return rpc


# test it
mycoin = coinrpc("../../bitcoin-0.10.2/bitcoin/bitcoin.conf")
bitcoinrpc = mycoin.rpccon()

print bitcoinrpc.getinfo()
