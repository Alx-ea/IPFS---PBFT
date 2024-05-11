# Practical Byzantine Fault Tolerance
PBFT is a consensus algorithm [used by some of the biggest Blockchains](https://blockonomi.com/practical-byzantine-fault-tolerance/).

It's known for being a more scalable alternative to the traditional [Proof of Work](https://en.wikipedia.org/wiki/Proof-of-work_system).

## Execution

Run scripts 1 - 3

```sh
./script_1_build_images_create_containers.sh
./script_2_get_ip_addresses.sh
./script_3_terminals_exec_pbft_nodes.sh
```

Otherwise:
 
## Docker Example

Building docker container for pbft and starting n nodes.

```sh
docker build . pbft/algo
docker-compose scale node=<total-num-of-nodes> #starts n containers
```

Let's see the steps to follow for n=4 nodes with 2 master nodes.

Use `docker ps` for viewing the container ids. To get the ip of the container processes use:

```sh
docker exec -it pbft_node_1 ip addr
docker exec -it pbft_node_2 ip addr
docker exec -it pbft_node_3 ip addr
docker exec -it pbft_node_4 ip addr
```

Copy the container ip:

```sh
docker exec -it pbft_node_1 node networkNode.js master full <container-ip> this
docker exec -it pbft_node_2 node networkNode.js master full <container-ip> <pbft_node_1's_IP>
docker exec -it pbft_node_3 node networkNode.js network full <container-ip> <pbft_node_1or2's_IP>
docker exec -it pbft_node_4 node networkNode.js network full <container-ip> <pbft_node_1or2's_IP>
```
These will start 2 master node and 2 network nodes.

### Interacting with blockchain

#### View

```sh
curl <node_ip>:3002/blockchain # for viewing the blockchain
```

#### Append

```sh
curl -XPOST <master_node_ip>:3002/createblock -H "Content-Type: application/json" -d '{
 "timestamp": "YYYY-MM-DD HH:MM:SS",  // optional
 "carPlate": "<plate>",
 "block": {
  "data": "any data, can be an array, or json, str..."
 }
}' # for creating a new block
```

#### View

```sh
curl <node_ip>:3002/blockchain # for viewing the blockchain after the adding of new block is completed
```

---

Further repositories of the CarChain Project:

[Blockchain Visualizer](https://github.com/LRAbbade/Blockchain-Visualizer)

[CarChain Dashboard](https://github.com/LRAbbade/CarChain-Dashboard)

[Car Simulator](https://github.com/LRAbbade/Car_Simulator)
