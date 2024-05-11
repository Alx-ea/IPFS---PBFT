#!/bin/bash

# Predefined values
n_nodes=3
ip_addresses=()

# Loop through container names to get and store ip addresses
for ((i=0; i<=n_nodes; i++)); do
  container_name1="ipfs$i"
#  container_name2="ipfs-cluster-$i"
  ip_address=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$container_name1")   # Use 'docker inspect' to get the IP address of the container
  ip_addresses+=("$ip_address")
 # ip_address=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$container_name2") 
#  ip_addresses+=("$ip_address")  # Add the IP address to the array
done

# Print the IP addresses
echo "IP addresses of the containers:"
for ip in "${ip_addresses[@]}"; do
  echo "$ip"
done
echo ${ip_addresses[@]}

# Export the variable to be used in the next script
export ip_addresses
