#!/bin/bash

# Predefined values
n_nodes=32
source script_2_get_ip_addresses.sh

# Print the IP addresses
echo "IP addresses of the containers:"
for ip in "${ip_addresses[@]}"; do
  echo "$ip"
done
echo "Array values: ${ip_addresses[@]}"

for ((i=1; i<=n_nodes; i++)); do
  if [ "$i" -eq 1 ]; then
    # Action for i = 1
    echo "Performing action for i = 1"
    command="sudo docker exec -it pbft_node_1 node networkNode.js master full ${ip_addresses[0]} this"
    echo $command
    # gnome-terminal -- bash -c "$command; exec bash" &
    gnome-terminal --tab --active -- bash -c "$command; exec bash" &
    sleep 5

  else
    echo "Performing action for i = $i"
    # echo ${ip_addresses[$((i-1))]}
    command="sudo docker exec -it pbft_node_$i node networkNode.js master full ${ip_addresses[$((i-1))]} ${ip_addresses[0]}"
    echo $command
    # gnome-terminal -- bash -c "$command; exec bash" &
    gnome-terminal --tab --active -- bash -c "$command; exec bash" &
    sleep 2
  fi
done
