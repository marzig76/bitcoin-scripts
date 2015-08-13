import sqlite3

class ratedata:

    def __init__(self):
        conn = sqlite3.connect('rates.db')
        c = conn.cursor()

    def rateinsert(self):



# Insert a row of data
#c.execute('delete from rate')
#c.execute('INSERT INTO rate VALUES (?,?,datetime())', ('BTC_LTC',66.5656))

for row in c.execute('SELECT min(rate), max(rate) FROM rate'):
    print row

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
