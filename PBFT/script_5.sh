#!/bin/bash

echo "hi"
for n_nodes in {1..3}; do
    echo "Running script with n_nodes=$n_nodes..."
    sed -i "s/n_nodes=11/n_nodes=$n_nodes/" script_1_build_images_create_containers.sh
    bash script_1_build_images_create_containers.sh
done
