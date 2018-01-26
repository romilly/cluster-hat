#! /usr/bin/python3


#
#  Synchronized subscriber
#

import time
import zmq
import picamera
import socket

def main():
    context = zmq.Context()

    # First, connect our subscriber socket
    subscriber = context.socket(zmq.SUB)
    subscriber.connect('tcp://controller:5561')
    subscriber.setsockopt(zmq.SUBSCRIBE, b'')

    time.sleep(1)

    # Second, synchronize with publisher
    syncclient = context.socket(zmq.REQ)
    syncclient.connect('tcp://controller:5562')

    # send a synchronization request
    syncclient.send(b'')

    # wait for synchronization reply
    syncclient.recv()

    hostname = socket.gethostname()
    camera = picamera.PiCamera()
    camera.hflip = True
    camera.vflip = True
    camera.resolution = (1280, 720)
    count = 0
    while True:
        msg = subscriber.recv()
        if msg == b'END':
            break
        jpg_count = '%s-image%d.jpg' % (hostname, count)
        # print('snap %s' % jpg_count)
        camera.capture(jpg_count)
        count += 1
    # print('done')




if __name__ == '__main__':
    main()
