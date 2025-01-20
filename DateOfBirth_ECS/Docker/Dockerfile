###############################################
# Base Image
###############################################
FROM public.ecr.aws/docker/library/python:3.8-slim-bullseye
FROM https://github.com/docker-library/python/blob/ebae24f3ea4df70859757829ac383e1dd8de3d2f/3.9/slim-bullseye/Dockerfile

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apt-get update
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    build-essential \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#RUN useradd -d /home/dcrusr -m -s /bin/bash dcrusr
#USER dcrusr

# Install pip and setuptools
RUN pip install --upgrade pip setuptools

# Remove pip after all packages are updated
#RUN python -m pip uninstall -y pip

###############################################
# Copy the code the app directory
###############################################
RUN mkdir /app
ADD . /app
WORKDIR /app

# Ensure the /app directory has the correct permissions
RUN chown -R root:root /app && chmod -R 755 /app

COPY Source .
COPY Source/requirements.txt .

# Install gunicorn
RUN pip install gunicorn


###############################################
# Installing Requirements
###############################################
RUN pip install --no-cache-dir -r requirements.txt
#RUN python -m spacy download en_core_web_sm

# Set the NLTK data path
#ENV NLTK_DATA /usr/local/share/nltk_data

# Download the NLTK data
#RUN python -m nltk.downloader -d /usr/local/share/nltk_data punkt
#RUN python -m nltk.downloader -d /usr/local/share/nltk_data wordnet
#RUN python -m nltk.downloader -d /usr/local/share/nltk_data stopwords

# Remove pip after all packages are updated
RUN python -m pip uninstall -y pip

# Create a group and user
#RUN useradd -ms /bin/bash appuser
RUN useradd -d /home/appuser -m -s /bin/bash appuser

# Ensure the /app directory has the correct permissions for appuser
RUN chown -R appuser:appuser /app && chmod -R 755 /app
USER appuser

Expose 8002

###############################################
# Set the command to run the Flask app with Gunicorn
###############################################
CMD ["gunicorn", "--timeout", "3600", "-w", "4", "--bind", "0.0.0.0:8002", "date_FlaskApi:app"]