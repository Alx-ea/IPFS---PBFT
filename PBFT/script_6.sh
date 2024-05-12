#!/bin/bash


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
