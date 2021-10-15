import pymysql
import mysql.connector
import sys
import boto3
import os
from dotenv import load_dotenv
from pathlib import Path

# ========= Env Variables =========
dotenv_path = Path('/Users/ianjpeck/Documents/GitHub/smashbrosgui/secrets.env')
load_dotenv(dotenv_path=dotenv_path)

# ========= Variables =========
endpoint = os.getenv('awsendpoint')
port = 3306
user = os.environ.get('awsuser')
password = os.environ.get('awspassword')
region = "us-east-2a"
dbname = os.environ.get('awsdb')

# ========= Functions =========
def query_sql(query):
    connection = pymysql.connect(host=endpoint, database=dbname, user=user, port=port, password=password)
    with connection:
        cur = connection.cursor()
        cur.execute(query)
        fighter = cur.fetchall()
        return fighter

# ========= Class? ===========
# class MySQLConnection:
#     def __init__(self, endpoint, user, password, port, region, dbname):
#         self.endpoint = endpoint
#         self.user = user
#         self.password = password
#         self.port = port
#         self.region = region
#         self.dbname = dbname
#         self.connection = None

#     def connect(self):
#         self.connection = pymysql.connect(host=self.endpoint, database=self.dbname, user=self.user, port=self.port, password=self.password)
#         return self.connection
    
#     def query(self, query):
#         with self.connection:
#             cur = self.connection.cursor()
#             data = cur.execute(query)
#             rows = data.fetchall()
#             return rows

