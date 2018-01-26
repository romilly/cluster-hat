import zmq
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://trespass:%s" % port)

while True:
    msg = socket.recv()
    print(msg)
    socket.send_unicode("client message to server1")
    socket.send_unicode("client message to server2")
    time.sleep(1)
