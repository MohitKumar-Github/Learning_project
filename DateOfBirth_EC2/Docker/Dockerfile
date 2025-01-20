FROM https://github.com/docker-library/python/blob/ebae24f3ea4df70859757829ac383e1dd8de3d2f/3.9/bullseye/Dockerfile
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY source ./source
EXPOSE 8002

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["uvicorn", "date_FlaskApi:app", "--host", "0.0.0.0", "--port", "8002"]