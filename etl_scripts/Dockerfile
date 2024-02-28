
FROM python:3.8-slim

# Install PostgreSQL command-line tools and sqlalchemy
#RUN apt-get update && apt-get install -y postgresql-client


RUN pip install SQLAlchemy && pip install psycopg2-binary

# Copy the ELT script 
COPY etl_script.py .

# Set the default command to run the ELT script
CMD ["python", "etl_script.py"]