import requests
import json
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object
cursor = db.cursor()

# Drop table if it already exists
cursor.execute("DROP TABLE IF EXISTS USER")

# Create table as per requirement
sql = """CREATE TABLE USER  (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `name` text NOT NULL,
          `email` varchar(120) NOT NULL
          PRIMARY KEY (`id`),
          UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

cursor.execute(sql)

sql2 = "SELECT 'name','email' FROM USER"

result = cursor.execute(sql2)

headers = {'content-type': 'application/json'}
url = 'https://www.intercom.com/api'

# params = {"Parameters such as the session key"}

data = json.dumps([{'name': row[0], 'email': row[1] } for row in result], indent=4)

##########  data is converted to json like format ############
# data = [
#     {
#         'name': 'user1',
#         'email': 'email1',
#     },
#     {
#         'name': 'user2',
#         'email': 'email2',
#     },
# ]

requests.post(url, json=data, headers=headers)

# disconnect
db.close()
