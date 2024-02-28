from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

print("Starting ETL")
#Define host configuration 
postsql_host_config = {"DB_NAME" : 'postgres',
                        "DB_USER" : 'postgres',
                        "DB_PASS" : 'secret',
                        "DB_HOST" : 'DW_postgres',
                        "DB_PORT" : '5440' }

conn_string = f'postgresql://{postsql_host_config["DB_USER"]}:{postsql_host_config["DB_PASS"]}@{postsql_host_config["DB_HOST"]}:{postsql_host_config["DB_PORT"]}/{postsql_host_config["DB_NAME"]}'

try:
# Connection Establishment
    SQLAlchemy_engine = create_engine(conn_string)

    print("Database connected successfully")

except SQLAlchemyError as err:
    print(f"SQLAlchemyError: {err}")


except Exception as err:
    print(f"Unexpected Error: {err}")
        


print("Ending ETL")
