from sqlalchemy import create_engine, Column, Integer, String, Enum, Float, Date, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import text
import enum


# declarative base class
class Base(DeclarativeBase):
    pass

class GenderEnum(enum.Enum):
    Male = 1
    Female = 2

class SalesFact (Base):
 
    __tablename__ = 'salesFact'

    invoice_id = Column(Integer, primary_key=True)
    unit_price = Column(Float)
    quantity = Column(Integer)
    tax_5_percent = Column(Float)
    total = Column(Float)
    cogs = Column(Float)
    gross_margin_percentage = Column(Float)
    branch_id = Column(String)
    customer_id = Column(String)



class BranchDim (Base):
    
    __tablename__  = 'branchDim'
    branch_surrogate_key = Column(Integer, primary_key=True)
    branch_id = Column(Integer, primary_key=True)


class CustomerDim(Base):
    __tablename__  = 'CustomerDim'
    customer_surrogate_key = Column(Integer, primary_key=True)
    gender = Column(Enum(GenderEnum))

class ProductDim(Base):
    __tablename__  = 'productDim'
    product_surrogate_key = Column(Integer, primary_key=True)
    product_line_detail = Column(String)

class PaymentDim(Base):
    __tablename__  = 'paymentDim'
    product_surrogate_key = Column(Integer, primary_key=True)
    product_line_detail = Column(String)
    
class DateDim(Base):
    __tablename__  = 'datetDim'
    date_surrogate_key = Column(Integer, primary_key=True)
    date_id = Column(String)

def connect_data_warehouse_DB_ORM():
    postsql_host_config = {"DB_NAME" : 'DW_db',
                            "DB_USER" : 'postgres',
                            "DB_PASS" : 'secret',
                            "DB_HOST" : 'DW_postgres',
                            "DB_PORT" : '5432'}
    conn_string = f'postgresql+psycopg2://{postsql_host_config["DB_USER"]}:{postsql_host_config["DB_PASS"]}@{postsql_host_config["DB_HOST"]}:{postsql_host_config["DB_PORT"]}/{postsql_host_config["DB_NAME"]}'

    SQLAlchemy_engine = create_engine(conn_string)
    Base.metadata.create_all(SQLAlchemy_engine)

    # return created tables
    with SQLAlchemy_engine.connect() as conn:
        result = conn.execute(text("select * from information_schema.tables where table_name = 'invoice'")).fetchall()
        print(result)