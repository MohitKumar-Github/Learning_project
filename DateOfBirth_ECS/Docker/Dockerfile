# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app/
COPY Source/date_FlaskApi.py /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8002 available to the world outside this container
EXPOSE 8002

# Define environment variable
ENV FLASK_APP=date_FlaskApi.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8002

# Run flask when the container launches
CMD ["flask", "run"]


#========================================
##FROM python
##WORKDIR /app

# Install the application dependencies
##COPY requirements.txt .
##RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
##COPY Source .
##EXPOSE 8002

# Setup an app user so the container doesn't run as the root user
##RUN useradd app
##USER app

#uvicorn for fastapi
#gunicorn for flaskapi
#CMD ["uvicorn", "date_FlaskApi:app", "--host", "0.0.0.0", "--port", "8002"]
##CMD ["gunicorn", "date_FlaskApi:app", "--host", "0.0.0.0", "--port", "8002"]