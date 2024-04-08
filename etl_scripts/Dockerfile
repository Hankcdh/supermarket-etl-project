
FROM python:3.8-slim

#Python Environment Variable 
ENV PYTHONUNBUFFERED=1
# Install PostgreSQL command-line tools and sqlalchemy
WORKDIR /usr/src/app

# Copy the ELT script 
# COPY etl_main.py .
RUN pip install SQLAlchemy && pip install psycopg2-binary
RUN pip install pandas
RUN pip install pytest

# Set the default command to run the ELT script
CMD [ "python" ,"-u",  "./dev/etl_main.py" ]
