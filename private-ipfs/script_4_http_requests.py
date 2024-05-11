import requests
import json
import time

def http_post_register_node(nodeAddress):

    url = 'http://' +  nodeAddress + ':3002/register-node'

    # Define the JSON payload
    payload = {
        "nodeAddress":nodeAddress,
        "nodeType":"master"
    }

    # Convert payload to JSON string
    json_payload = json.dumps(payload)

    # Set the headers for the request
    headers = {
        'Content-Type': 'application/json'
    }

    # Perform the HTTP POST request
    response = requests.post(url, data=json_payload, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        print("HTTP POST register-node request was successful.")
        print(response.content.decode('utf-8'))
    else:
        print("HTTP POST register-node request failed with status code:", response.status_code)

def http_post_deregister_node(nodeAddress):

    url = 'http://' +  nodeAddress + ':3002/deregister-node'

    # Define the JSON payload
    payload = {
        "nodeAddress":nodeAddress
    }

    # Convert payload to JSON string
    json_payload = json.dumps(payload)

    # Set the headers for the request
    headers = {
        'Content-Type': 'application/json'
    }

    # Perform the HTTP POST request
    response = requests.post(url, data=json_payload, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        print("HTTP POST deregister-node request was successful.")
        print(response.content.decode('utf-8'))
    else:
        print("HTTP POST deregister-node request failed with status code:", response.status_code)

def http_post_create_block(nodeAddress, timestamp, carPlate, data):

    url = 'http://' +  nodeAddress + ':3002/createBlock'

    # Define the JSON payload
    payload = {
        "timestamp": timestamp,
        "carPlate": carPlate,
        "block": {
            "data": data
        }
    }

    # Convert payload to JSON string
    json_payload = json.dumps(payload)

    # Set the headers for the request
    headers = {
        'Content-Type': 'application/json'
    }

    # Perform the HTTP POST request
    try:    
        response = requests.post(url, data=json_payload, headers=headers, timeout=5)
        print(f'Response status code: {response.status_code}')
         # Check the response status code
        if response.status_code == 200:
            print("HTTP POST createBlock request was successful.")
            print(response.content.decode('utf-8'))
            with open("Output_20.txt", "a") as file:  # Use "a" mode for appending
                file.write(response.content.decode('utf-8') + "\n")  # Append the response content to the file
                print("Response data appended to 'Output_20.txt'")
        else:
            print("HTTP POST createBlock request failed with status code:", response.status_code)

    except requests.Timeout:
        # Handle timeout error
        print('Timeout occurred during POST request, moving on to the next line of code')
    
    except requests.RequestException as e:
        # Handle other request errors
        print(f'Error occurred during POST request: {e}')


def test():
    for _ in range(100):
        http_post_create_block("172.18.0.2","2020-01-01 00:00:00", "Car1", "Data1")

    # Return the output as a string
    return "Test completed successfully."

test()