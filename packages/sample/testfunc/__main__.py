import psycopg
from dotenv import load_dotenv
import os

# Specify the path to your .env file
#env_path = '.env'

# Load your .env file
load_dotenv()

def main(event, context):
    with psycopg.connect(dbname=os.environ['DATABASE'], user=os.environ['USERNAME'], password=os.environ['PASSWORD'], host=os.environ['HOST'], port=os.environ['PORT']) as conn:

    # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Execute a command: this creates a new table
        # Execute a command: this creates a new table
            cur.execute("""
                CREATE TABLE test (
                    id serial PRIMARY KEY,
                    num integer,
                    data text)
                """)
        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
            cur.execute(
                "INSERT INTO test (num, data) VALUES (%s, %s)",
                (100, "abc'def"))
            
            cur.execute("SELECT * FROM test")
            cur.fetchone()
            # will return (1, 100, "abc'def")

            # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
            # of several records, or even iterate on the cursor
            for record in cur:
                print(record)
            conn.commit()
    return {"body": 'Hello there'}
