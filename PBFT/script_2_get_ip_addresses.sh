#!/bin/bash

# Predefined values
n_nodes=4
ip_addresses=()

# Loop through container names to get and store ip addresses
for ((i=1; i<=n_nodes; i++)); do
  container_name="pbft_node_$i"
  ip_address=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$container_name")   # Use 'docker inspect' to get the IP address of the container
  ip_addresses+=("$ip_address")  # Add the IP address to the array
done

# Print the IP addresses
echo "IP addresses of the containers:"
for ip in "${ip_addresses[@]}"; do
  echo "$ip"
done
echo ${ip_addresses[@]}

# Export the variable to be used in the next script
export ip_addresses
