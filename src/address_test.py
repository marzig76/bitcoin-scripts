from block import block
from script import script
from blockutil import pkhash2addr
from blockutil import pubkey2addr

blockfile = '/home/marzig76/.bitcoin/blocks/blk00004.dat'
blockstream = open(blockfile, 'rb')
b = block(blockstream)

for t in b.txs:

    for ti in t.tx_inputs:
        print 'in addr: ' + pubkey2addr(ti.sigscript)

    for to in t.tx_outputs:
        spk = to.script_pk.encode('hex')

        if spk[:6] == '76a914':
            print 'out addr: ' + pkhash2addr(spk[6:46])
