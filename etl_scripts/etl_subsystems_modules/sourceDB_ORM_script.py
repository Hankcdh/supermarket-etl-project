
from sqlalchemy import create_engine, Column, Integer, String, Enum, Float, Date, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import text
import enum


# declarative base class
class Base(DeclarativeBase):
    pass


class CustomerEnum(enum.Enum):
    Normal = 1
    Member = 2

class GenderEnum(enum.Enum):
    Male = 1
    Female = 2
class PaymentEnum(enum.Enum):
    Cash = 1
    CreditCard = 2
    Ewallet = 3

class Invoice (Base):
 
    __tablename__ = 'invoice'

    invoice_id = Column(Integer, primary_key=True)
    branch = Column(String)
    city = Column(String)
    customer_type = Column(Enum(CustomerEnum))
    gender = Column(Enum(GenderEnum))
    product_line = Column(String)
    unit_price = Column(Float)
    quantity = Column(Integer)
    tax = Column(Float)
    total = Column(Float)
    date = Column(Date)
    time = Column(DateTime)
    payment = Column(Enum(PaymentEnum))
    cogs = Column(Float)
    gross_margin_percentage = Column(Float)
    # Excluded columns
    # gross_income = Column(Float)
    # rating = Column(Integer)

    


def connect_sourceDB_ORM():
    postsql_host_config = {"DB_NAME" : 'stage_db',
                            "DB_USER" : 'postgres',
                            "DB_PASS" : 'secret',
                            "DB_HOST" : 'stage_postgres',
                            "DB_PORT" : '5432'}
    conn_string = f'postgresql+psycopg2://{postsql_host_config["DB_USER"]}:{postsql_host_config["DB_PASS"]}@{postsql_host_config["DB_HOST"]}:{postsql_host_config["DB_PORT"]}/{postsql_host_config["DB_NAME"]}'

    SQLAlchemy_engine = create_engine(conn_string)
    Base.metadata.create_all(SQLAlchemy_engine)

    # return created tables
    with SQLAlchemy_engine.connect() as conn:
        result = conn.execute(text("select * from information_schema.tables where table_name = 'invoice'")).fetchall()
        print(result)