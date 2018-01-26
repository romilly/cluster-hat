#!/usr/bin/env bash
cd ~/git/active/cluster-hat/src/python/spikes/zmqspike/
file=$1
shift
for dest in "$@"
    do
        scp $file pi@$dest:
        ssh pi@$dest "chmod a+x $file"
done