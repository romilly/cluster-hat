#! /usr/bin/python3

import zmq
import time

SUBSCRIBERS_EXPECTED = 2
STEREO_PAIRS_TO_TAKE = 3

def main():
    context = zmq.Context()

    publisher = context.socket(zmq.PUB)
    publisher.sndhwm = 1100000
    publisher.bind('tcp://*:5561')

    syncservice = context.socket(zmq.REP)
    syncservice.bind('tcp://*:5562')

    subscribers = 0
    while subscribers < SUBSCRIBERS_EXPECTED:
        msg = syncservice.recv()
        syncservice.send(b'')
        subscribers += 1

    for i in range(STEREO_PAIRS_TO_TAKE):
        publisher.send(b'say cheese')
        time.sleep(1)
    publisher.send(b'END')

if __name__ == '__main__':
    main()
