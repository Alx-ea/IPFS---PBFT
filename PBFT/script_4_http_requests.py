import requests
import json
import time

def http_post_register_node(nodeAddress):
    url = 'http://' + nodeAddress + ':3002/register-node'
    payload = {
        "nodeAddress": nodeAddress,
        "nodeType": "master"
    }
    json_payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=json_payload, headers=headers)
    if response.status_code == 200:
        print("HTTP POST register-node request was successful.")
        print(response.content.decode('utf-8'))
    else:
        print("HTTP POST register-node request failed with status code:", response.status_code)

def http_post_deregister_node(nodeAddress):
    url = 'http://' + nodeAddress + ':3002/deregister-node'
    payload = {
        "nodeAddress": nodeAddress
    }
    json_payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=json_payload, headers=headers)
    if response.status_code == 200:
        print("HTTP POST deregister-node request was successful.")
        print(response.content.decode('utf-8'))
    else:
        print("HTTP POST deregister-node request failed with status code:", response.status_code)

def http_post_create_block(nodeAddress, timestamp, patientId, bodyTemp, pulseRate, respirationRate, bloodOxygen, glucoseLevel):
    url = 'http://' + nodeAddress + ':3002/createBlock'
    payload = {
        "timestamp": timestamp,
        "patientId": patientId,
        "block": {
            "vitals": {
                "bodyTemp": bodyTemp,
                "pulseRate": pulseRate,
                "respirationRate": respirationRate,
                "bloodOxygen": bloodOxygen,
                "glucoseLevel": glucoseLevel
            }
        }
    }
    json_payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, data=json_payload, headers=headers, timeout=5)
        print(f'Response status code: {response.status_code}')
        if response.status_code == 200:
            print("HTTP POST createBlock request was successful.")
            print(response.content.decode('utf-8'))
            with open("Output_20.txt", "a") as file:
                file.write(response.content.decode('utf-8') + "\n")
                print("Response data appended to 'Output_20.txt'")
        else:
            print("HTTP POST createBlock request failed with status code:", response.status_code)
    except requests.Timeout:
        print('Timeout occurred during POST request, moving on to the next line of code')
    except requests.RequestException as e:
        print(f'Error occurred during POST request: {e}')

def test():
    # Example usage with patient data
    for _ in range(100):
        http_post_create_block("172.18.0.2", "2024-05-10 00:00:00", "Patient1234", 36.6, 72, 16, 98, 140)
    return "Test completed successfully."

# Call the test function
test()
