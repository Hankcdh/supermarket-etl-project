
import pandas as pd
import numpy as np 
import pytest 
from numpy import nan 
from  etl_script import extract_sourceCSV , transform_sourceCSV, load_sourceCSV_to_sourceDB



# get data
@pytest.fixture(scope='session', autouse=True)
def source_ETL():
    df_source = extract_sourceCSV()
    yield df_source
    df_transform = transform_sourceCSV(df_source)
    load_sourceCSV_to_sourceDB(df_transform)


# check if column exists
def test_col_exists(source_ETL):
    name="invoice_id"
    name2 ="Unit price"
    assert name in source_ETL.columns
    assert name2 in source_ETL.columns

# check for nulls
def test_null_check(source_ETL):
    assert source_ETL['invoice_id'].notnull().all()

# check values are unique
def test_unique_check(source_ETL):
    assert pd.Series(source_ETL['invoice_id']).is_unique

# check data type
def test_productkey_dtype_int(source_ETL):
    assert (source_ETL['invoice_id'].dtype == str or source_ETL['invoice_id'].dtype == 'O')

# check data type
def test_productname_dtype_srt(source_ETL):
    assert (source_ETL['Branch'].dtype == str or  source_ETL['Branch'].dtype == 'O')

# check values in range
def test_range_val(source_ETL):
    assert source_ETL['Unit price'].between(0,1000).any()

# check values in a list
def test_range_val_str(source_ETL):
    gener_enum = {'Male' ,'Female'}
    assert source_ETL['Gender'].isin(gener_enum).all()