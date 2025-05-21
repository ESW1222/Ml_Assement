# Use official Python image from DockerHub
FROM python:3.8-slim

# Set working directory in the container
WORKDIR /app

# Copy current directory contents to the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Command to run the app
CMD ["python", "app/main.py"]
