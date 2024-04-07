from etl_subsystems_modules import etl_script
from etl_subsystems_modules import sourceDB_ORM_script
import subprocess 


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
try:
    target_directory = "./dev/etl_subsystems_modules"
    result = subprocess.run(["python" , "-m" , "pytest" ,"-v"] , check=True , capture_output=True, text=True, cwd=target_directory )
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error in source data not passing quality test: {e}")
    print(e.stdout)
    exit(1)
# df_source = etl_script.extract_sourceCSV()
# df_transformed = etl_script.transform_sourceCSV(df_source)
# etl_script.load_sourceCSV_to_sourceDB(df_transformed)




