import psycopg2
from dotenv import load_dotenv
import os

# Specify the path to your .env file
#env_path = '.env'

# Load your .env file
load_dotenv()

def main(event, context):
    connection = psycopg2.connect(database=os.environ['DATABASE'], user=os.environ['USERNAME'], password=os.environ['PASSWORD'], host=os.environ['HOST'], port=os.environ['PORT'])
    cursor = connection.cursor()
    return {"body": 'Hello there'}
