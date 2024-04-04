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
    print("Connecting SourceDB  with ORM Applied")
    postsql_host_config = {"DB_NAME" : 'stage_db',
                            "DB_USER" : 'postgres',
                            "DB_PASS" : 'secret',
                            "DB_HOST" : 'stage_postgres',
                            "DB_PORT" : '5432'}
    conn_string = f'postgresql+psycopg2://{postsql_host_config["DB_USER"]}:{postsql_host_config["DB_PASS"]}@{postsql_host_config["DB_HOST"]}:{postsql_host_config["DB_PORT"]}/{postsql_host_config["DB_NAME"]}'
    SQLAlchemy_engine = create_engine(conn_string)
    print("Extracting from CSV to source DB")
    
    #Transformation Matching df column names to ORM names 
    #alternative method using python.rename() function with dictionary 

    #transform all names into lower cases
    df.columns = map(str.lower, df.columns)
    #Replace all names with space with 
    df.columns = map(lambda x: x.replace(' ', '_'), df.columns)
    #replace 'tax_5%'  to  tax_5_percemt
    df = df.rename(columns={"tax_5%" : "tax_5_percent"})
    #drop excluded columns : gross income and rating
    df = df.drop(columns=['gross_income' , 'rating'])
    

    #Transforming all data types to match ORM
    #remove '-'from invoice_id
    df['invoice_id'] = df['invoice_id'].apply(lambda x: x.replace('-',''))
    print(df['invoice_id'])

    #alterte data and time to DateTime
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    df = df.drop(columns=['date','time'])
    print(df.dtypes)

    #update payment type values 'Credit Card' to 'CreditCard' 
    df['payment'] = df['payment'].replace('Credit card' , 'CreditCard')

    # Load the dataframe to the stage_db in postgreSQL
    print(df)
    df.to_sql(name='invoice', con=SQLAlchemy_engine , if_exists='append' , index=False)


    print("Returning Reslults FROM SourceDB")
    with SQLAlchemy_engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM invoice LIMIT 5")).fetchall()
        print(result)
   

   


