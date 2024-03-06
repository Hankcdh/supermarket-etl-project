
FROM python:3.8-slim

# Install PostgreSQL command-line tools and sqlalchemy
#RUN apt-get update && apt-get install -y postgresql-client
WORKDIR /usr/src/app

# Copy the ELT script 
COPY . .

RUN pip install SQLAlchemy && pip install psycopg2-binary

# Set the default command to run the ELT script
CMD ["python", "etl_main.py"]
