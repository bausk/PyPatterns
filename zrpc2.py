__author__ = 'bausk'

import zmq
import time
import msgpack

print("server starting...\n")

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://0.0.0.0:4242")

while True:
    #  Wait for next request from client
    message = socket.recv()
    m2 = msgpack.unpackb(message)
    print "Received request: ", message
    time.sleep(1)
    socket.send("World from 4242")

print("Work complete.\n")
