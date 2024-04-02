from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import literal_column
from sqlalchemy.exc import SQLAlchemyError
import time 
import pandas as pd
import subprocess
from sqlalchemy import text
import json

def initialise_connection_to_DestinationDB(max_retries=5, delay_seconds=5):
    print("Starting Initialisation DestinationDB")
    #Define host configuration 
    postsql_host_config = {"DB_NAME" : 'DW_db',
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
            print("Connection successful to DestinationDB!")
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
    print("Failed to connect to DestinationDB")
    return False


def initialise_connection_to_SourceDB(max_retries=5, delay_seconds=5):
    print("Starting Initialisation SourceDB")
    #Define host configuration 
    postsql_host_config = {"DB_NAME" : 'stage_db',
                            "DB_USER" : 'postgres',
                            "DB_PASS" : 'secret',
                            "DB_HOST" : 'stage_postgres',
                            "DB_PORT" : '5432'}

    conn_string = f'postgresql+psycopg2://{postsql_host_config["DB_USER"]}:{postsql_host_config["DB_PASS"]}@{postsql_host_config["DB_HOST"]}:{postsql_host_config["DB_PORT"]}/{postsql_host_config["DB_NAME"]}'
    
    retries = 0
    while retries < max_retries:
        try:
        # Connection Establishment
            SQLAlchemy_engine = create_engine(conn_string)
            connection = SQLAlchemy_engine.connect()
            print("Connection successful to SourceDB!")
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
    print("Failed to connect to SourceDB")
    return False


def extract_CSV_to_sourceDB():
    print("extracting data")
    df = pd.read_csv("./dev/source_data/supermarket_sales_samples.csv")
    postsql_host_config = {"DB_NAME" : 'stage_db',
                            "DB_USER" : 'postgres',
                            "DB_PASS" : 'secret',
                            "DB_HOST" : 'stage_postgres',
                            "DB_PORT" : '5432'}
    conn_string = f'postgresql+psycopg2://{postsql_host_config["DB_USER"]}:{postsql_host_config["DB_PASS"]}@{postsql_host_config["DB_HOST"]}:{postsql_host_config["DB_PORT"]}/{postsql_host_config["DB_NAME"]}'
    SQLAlchemy_engine = create_engine(conn_string)

    print("Extracting from CSV to source DB")
    df.to_sql(name='invoice', con=SQLAlchemy_engine , if_exists='replace')

    print("Returning Reslults FROM SourceDB")
    with SQLAlchemy_engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM invoice LIMIT 5")).fetchall()
        print(result)
   
    
