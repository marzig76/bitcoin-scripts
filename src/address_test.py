from block import block
from script import script
import sqlite3

blockfile = '/home/marzig76/.bitcoin/blocks/blk00004.dat'
blockstream = open(blockfile, 'rb')
b = block(blockstream)

for t in b.txs:

  for ti in t.tx_inputs:
    ti.sigscript.encode('hex')

  for to in t.tx_outputs:
