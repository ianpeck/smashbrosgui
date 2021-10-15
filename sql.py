import pymysql
import mysql.connector
import sys
import boto3
import os

# ========= Variables =========
endpoint = os.environ.get('awsendpoint')
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
