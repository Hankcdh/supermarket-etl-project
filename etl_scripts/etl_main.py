from etl_subsystems_modules import etl_script




print("Startig etl_main")

# Initailisting connection 
# Connection Quality Check 


print("start Quality Checks")
if not etl_script.initialise_connection_to_DestinationDB() & etl_script.initialise_connection_to_SourceDB():
    exit(1)

#extracting source data from CSV format into stage database -> SourceDB
etl_script.extract_CSV_to_sourceDB()

print("Ending etl_main")


