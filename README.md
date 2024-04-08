# Debug postgresql using psql 
- command run in docker main directory 
- checking out target postgres content "target_DB_name"
    - command : docker exec -it "target_DB_name" psql -U postgres 

- PSQL commands
    - check database : \dt
    - check current connected db : \c 
    - check table column and data type : \d "table_name"
    - check tables and schemas using information_schema.columns : 
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'public' AND table_name = 'staff_info';

# Debug Docker Directories using subprocess
- running shell commands using subprocess in python 
- commands:
    - check current directory : 
        # Execute the command to get the current directory
        result = subprocess.run(["pwd"], capture_output=True, text=True)

        # Print the output
        print("Current Directory:", result.stdout.strip())