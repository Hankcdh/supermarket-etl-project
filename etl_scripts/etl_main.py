from etl_subsystems_modules import etl_script
from etl_subsystems_modules import sourceDB_ORM_script


import subprocess 
from sqlalchemy.exc import SQLAlchemyError



print("Startig etl_main")
# Initailisting connection 
# Connection Quality Check 


print("start Quality Checks")
if not etl_script.initialise_connection_to_DestinationDB() & etl_script.initialise_connection_to_SourceDB():
    exit(1)

#Create ORM mapping to the sourceDB
sourceDB_ORM_script.connect_sourceDB_ORM()


#pytesting the pipeline and execute
#extracting source data from CSV format into stage database -> SourceDB

# if not etl_script.source_test():
#     print("notifying source system SME....")
#     exit(1)

# try:
#     df_source = etl_script.extract_sourceCSV()
#     df_transformed = etl_script.transform_sourceCSV(df_source)
#     etl_script.load_sourceCSV_to_sourceDB(df_transformed)
# except SQLAlchemyError as err:
#             print(f"SQLAlchemyError: {err}")
    


#Create ORM mapping to the Data Warehouse Database 
# Data_Warehouse_DB_ORM.connect_data_warehouse_DB_ORM()
dimTables_file_path = '/usr/src/app/dev/sql/dimTables.sql'
factTable_file_path = '/usr/src/app/dev/sql/factTable.sql'
etl_script.implement_data_warehouse_model_sql(dimTables_file_path)
etl_script.implement_data_warehouse_model_sql(factTable_file_path)


