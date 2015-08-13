import sqlite3


conn = sqlite3.connect('rates.db')
c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE rate (pair text, rate real, dtg text)''')

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
