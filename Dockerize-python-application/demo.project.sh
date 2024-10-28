#!/bin/bash

# Build the Docker image
docker build -t my-flask-app .

# Run the Docker container
docker run -d -p 5000:5000 my-flask-app

echo "Wait 20s for application up"
sleep 20

# Verify the result

curl localhost:5000