from block import block
from script import script
import sqlite3

blockfile = '/home/marzig76/.bitcoin/blocks/blk00004.dat'
blockstream = open(blockfile, 'rb')
b = block(blockstream)

# create db connection
conn = sqlite3.connect('../blexplor-web/db.sqlite3')
c = conn.cursor()

# insert block
insert_block = (
    "INSERT INTO block_block " +
    "(magic_number, block_size, version, prev_hash, merkel_root, " +
    "block_time, target, nonce, tx_count, block_height)" +
    "VALUES " +
    "(?,?,?,?,?,?,?,?,?,0)"
)
c.execute(insert_block, (b.magic_number, b.block_size, b.version, b.prev_hash,
                         b.merkel_root, b.time, b.target, b.nonce, b.txcount))
conn.commit()

# get last block id
result = conn.execute("SELECT max(id) FROM block_block")
for row in result:
    block_id = row[0]

# insert each tx
for t in b.txs:
    # insert tx
    insert_tx = (
        "INSERT INTO block_tx " +
        "(version, tx_input_count, tx_output_count, lock_time, block_id)" +
        "VALUES " +
        "(?,?,?,?,?)"
    )
    c.execute(insert_tx, (t.version, t.tx_input_count, t.tx_output_count,
                          t.lock_time, block_id))
    conn.commit()

    # get last tx id
    result = conn.execute("SELECT max(id) FROM block_tx")
    for row in result:
        tx_id = row[0]

    # insert each tx_input
    for ti in t.tx_inputs:
        insert_txinput = (
            "INSERT INTO block_txinput " +
            "(prev_hash, `index`, script_bytes, sigscript, sequence, tx_id)" +
            "VALUES " +
            "(?,?,?,?,?,?)"
        )
        c.execute(insert_txinput, (ti.prev_hash, ti.index, ti.script_bytes,
                                   ti.sigscript.encode('hex'), ti.sequence,
                                   tx_id))
        conn.commit()

    # insert each tx_output
    for to in t.tx_outputs:
        insert_txoutput = (
            "INSERT INTO block_txoutput " +
            "(value, script_pk_bytes, script_pk, tx_id)" +
            "VALUES " +
            "(?,?,?,?)"
        )
        c.execute(insert_txoutput, (to.value, to.script_pk_bytes,
                                    to.script_pk.encode('hex'), tx_id))
        conn.commit()
