# Vegetable Filtering Microservice
# Quinn Downey
# 2025/05/17
#
# This microservice utilizes a json file of vegetable data 
# to find all vegetables that match a specific category 
# or growing season, as requested by the client.


import time
import zmq
import json


# set up ZMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# get veggie data
file = open("vegetable_data.json")
veg_data = json.load(file)
file.close()

print("Waiting for request from client...")
while True:
    message = socket.recv()
    filter = message.decode().lower()

    print(f"\nReceived from client: {filter}")

    results = []

    for veg in veg_data:
        if veg["Season"].lower().find(filter) != -1 or veg["Season"] == "Year-round":
            results.append(veg["Name"])

        elif veg["Category"].lower() == filter.lower():
            results.append(veg["Name"])

    print("Filter results:", results)

    time.sleep(1)

    print("Sending results to client...")

    if len(results) == 0:
        socket.send_string("No data found.")
    else:
        socket.send_string(str(results))
