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

# ========= Functions =========n
def query_sql(query):
    connection = pymysql.connect(host=endpoint, database=dbname, user=user, port=port, password=password)
    with connection:
        cur = connection.cursor()
        cur.execute(query)
        fighter = cur.fetchall()
        return fighter
