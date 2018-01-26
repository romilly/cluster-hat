#! /usr/bin/python3

#
#  Synchronized publisher
#
import zmq
import time

#  We wait for 2 subscribers
SUBSCRIBERS_EXPECTED = 2

def main():
    context = zmq.Context()

    # Socket to talk to clients
    publisher = context.socket(zmq.PUB)
    # set SNDHWM, so we don't drop messages for slow subscribers
    publisher.sndhwm = 1100000
    publisher.bind('tcp://*:5561')

    # Socket to receive signals
    syncservice = context.socket(zmq.REP)
    syncservice.bind('tcp://*:5562')

    # Get synchronization from subscribers
    subscribers = 0
    while subscribers < SUBSCRIBERS_EXPECTED:
        # wait for synchronization request
        msg = syncservice.recv()
        # send synchronization reply
        syncservice.send(b'')
        subscribers += 1
        # print("+1 subscriber (%i/%i)" % (subscribers, SUBSCRIBERS_EXPECTED))


    for i in range(3):
        publisher.send(b'say cheese')
        time.sleep(1)
    publisher.send(b'END')
    # print('done')

if __name__ == '__main__':
    main()
