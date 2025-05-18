# This little program is for testing the functionality of 
# the Veggie Filtering microservice.


import zmq


context = zmq.Context()
print("\nTest client attempting to connect to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    test_filter = input("\nEnter filter to test: ")

    print(f"\nRequesting data for: {test_filter}")
    socket.send_string(test_filter)

    message = socket.recv()
    print(f"\nServer sent: {message.decode()}")
