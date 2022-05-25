import pymysql
import os
from dotenv import load_dotenv
from pathlib import Path

# ========= Env Variables =========
dotenv_path = Path('secrets.env')
load_dotenv(dotenv_path=dotenv_path)

# ========= Variables =========
endpoint = os.getenv('awsendpoint')
port = 3306
user = os.environ.get('awsuser')
password = os.environ.get('awspassword')
region = "us-east-2a"
dbname = os.environ.get('awsdb')

# ========= Functions =========
def h2h_query_sql(query):
    connection = pymysql.connect(host=endpoint, database=dbname, user=user, port=port, password=password)
    with connection:
        cur = connection.cursor()
        cur.execute(query)
        fighter_data = cur.fetchone()
        fighter1_dict = {}
        fighter2_dict = {}
        # Parse One Line Tuple
        for i, data in enumerate(fighter_data):
            if i == 0:
                fighter1_dict['Fighter'] = data
            elif i == 1:
                fighter1_dict['Wins'] = str(data)
                fighter2_dict['Losses'] = str(data)
            elif i == 2:
                fighter1_dict['W/L %'] = data
            elif i == 3:
                fighter2_dict['Fighter'] = data
            elif i == 4:
                fighter2_dict['Wins'] = str(data)
                fighter1_dict['Losses'] = str(data)
            elif i == 5:
                fighter2_dict['W/L %'] = data
        return [fighter1_dict, fighter2_dict]

def select_list(query, columnnumber):
    connection = pymysql.connect(host=endpoint, database=dbname, user=user, port=port, password=password)
    with connection:
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        dataList = []
        for row in data:
            dataList.append(row[columnnumber])
        return dataList

def select_view_row(query):
    connection = pymysql.connect(host=endpoint, database=dbname, user=user, port=port, password=password)
    with connection:
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        dataList = []
        for row in data:
            dataList.append(row)
        return dataList
