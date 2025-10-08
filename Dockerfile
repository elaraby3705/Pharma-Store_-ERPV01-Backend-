# Use a Python base image (Factor I: Codebase)
# We choose a slim version for a smaller container size
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Ensure logs are buffered to standard output for Factore XI (Logs)

ENV PYTHONUNBUFFERED 1

# 1. intall Dependencies
# Copy requirements file first to take advantage of Docker cache layers
# This prevents reinstalling dependencies every time the code changes

COPY COPY requirements.txt /app/

# Install Python dependencies

RUN pip install --no-cache-dir -r requirements.txt

# 3. Expose Port
# Factor VII (Port Binding): Expose the port where Gunicorn/Django will run
EXPOSE 8000

# 4. Define Startup Command (Factor V: Build, Release, Run)
# This uses Gunicorn (the production server) as the entry point.
# Note: We will use 'docker-compose.yml' to override this for local development commands like 'manage.py runserver'.
CMD ["gunicorn", "pharma_store_v01.wsgi:application", "--bind", "0.0.0.0:8000"]