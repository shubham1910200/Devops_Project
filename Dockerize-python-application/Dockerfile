# Dockerfile

# Use the Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the host
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
