#!/bin/bash

# Predefined values
n_nodes=4

# Stop and remove containers one by one
container_ids=$(docker ps -aq)
echo "Container IDs:"
echo "$container_ids"
for container_id in $container_ids; do
    echo "Stopping container $container_id..."
    docker stop $container_id
    echo "Removing container $container_id..."
    docker rm $container_id
done
echo "All containers stopped and removed."

# Remove all exisitng images by force
docker image rm -f $(docker images -a -q)

# Build a new image based on the amended code
sudo docker build . -t pbft
if [ "$?" -eq 0 ]; then
  echo "Docker build successful."
else
  echo "Docker build failed."
  exit 1
fi

# Create network if needed
sudo docker network create pbft_default
if [ "$?" -eq 0 ]; then # Check if the previous command was successful
  echo "Docker network created successfully."
else
  echo "Docker network creation failed."
#   exit 1
fi

# Create desired number of comntainers
command="sudo docker-compose scale node=$n_nodes" # Define the command as a string
eval $command # Run the command using eval
if [ "$?" -eq 0 ]; then # Check if the previous command was successful
  echo "Docker compose scale successful."
else
  echo "Docker compose scale failed."
  exit 1
fi

# Print the final outcome
echo "All commands executed successfully."
