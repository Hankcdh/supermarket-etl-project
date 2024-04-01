from etl_subsystems_modules import etl_script
import time



print("Startig etl_main")

# Initailisting connection 
# Connection Quality Check 



print("start Quality Checks")
if not etl_script.initialise_connection_to_DestinationDB() & etl_script.initialise_connection_to_SourceDB():
    exit(1)



print("Ending etl_main ")


