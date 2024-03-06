from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import literal_column
from sqlalchemy.exc import SQLAlchemyError
import time 


def initialise_connection(max_retries=5, delay_seconds=5):
    print("Starting Initialisation")
    #Define host configuration 
    postsql_host_config = {"DB_NAME" : 'stage_db',
                            "DB_USER" : 'postgres',
                            "DB_PASS" : 'secret',
                            "DB_HOST" : 'DW_postgres',
                            "DB_PORT" : '5432'}

    conn_string = f'postgresql+psycopg2://{postsql_host_config["DB_USER"]}:{postsql_host_config["DB_PASS"]}@{postsql_host_config["DB_HOST"]}:{postsql_host_config["DB_PORT"]}/{postsql_host_config["DB_NAME"]}'
    
    retries = 0
    while retries < max_retries:
        try:
        # Connection Establishment
            SQLAlchemy_engine = create_engine(conn_string)
            connection = SQLAlchemy_engine.connect()
            print("Connection successful!")
            connection.close() 
            return True
        except SQLAlchemyError as err:
            print(f"SQLAlchemyError: {err}")
            retries += 1
            print(
                f"Retrying in {delay_seconds} seconds... (Attempt {retries}/{max_retries})")
            time.sleep(delay_seconds)

        except Exception as err:
            print(f"Unexpected Error: {err}")
    print("Max retries reached. Exiting.")
    return False


    
