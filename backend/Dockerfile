# Use the official Python image as a base
FROM python:3.10-slim

# Set environment variables
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container
COPY . .

# Ensure the migrations folder exists (for persistence)
RUN mkdir -p /app/migrations

# Install Flask-Migrate if it's not installed yet
RUN pip install flask-migrate

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Specify the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Command to run the application
CMD ["flask", "run"]
