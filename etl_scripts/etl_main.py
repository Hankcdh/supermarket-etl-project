from etl_subsystems_modules import etl_script
import time





# Use the function before running the ELT process


print("Startig etl_main")

if not etl_script.initialise_connection():
    exit(1)

print("Ending etl_main ")


