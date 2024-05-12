#!/bin/bash

# Network name
NETWORK_NAME="shared_network"

# Check if the network exists
if ! docker network ls | grep -wq $NETWORK_NAME; then
  echo "Network $NETWORK_NAME does not exist, creating it..."
  docker network create $NETWORK_NAME
fi

# Get all running container IDs
container_ids=$(docker ps -q)

# Connect each container to the specified network
for id in $container_ids; do
  echo "Connecting container $id to network $NETWORK_NAME..."
  docker network connect $NETWORK_NAME $id
done

echo "All containers have been connected to $NETWORK_NAME."

