import json
import time
import sqlite3
from restful_lib import Connection

# setup db
sqlconn = sqlite3.connect('rates.db')
c = sqlconn.cursor()

# connect to shapeshift
base_url = "https://shapeshift.io"
ssconn = Connection(base_url)

rate = "btc_ltc"
ssrate = "/rate/" + rate
while 1:
    # checking exchange rate
    btc_ltc_rate = ssconn.request(ssrate)

    # extract the body of the response
    for item in btc_ltc_rate:
        if item == "body":
            response = json.loads(btc_ltc_rate[item])

    # extract the rate
    for key, value in response.iteritems():
        if key == "rate":
            c.execute('INSERT INTO rate VALUES (?,?,datetime())', (rate,value))
            sqlconn.commit()

    time.sleep(60)
