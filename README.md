# Debug postgresql using psql 
- command run in docker main directory 
- checking out target postgres content "target_DB_name"
    - command : docker exec -it "target_DB_name" psql -U postgres 

- PSQL commands
    - check database : \dt
    - check current connected db : \c 