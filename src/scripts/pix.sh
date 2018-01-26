#!/usr/bin/env bash
sleep 10s
echo 'say cheese!'
ssh pi@P1 "./zsub.py" &
ssh pi@P2 "./zsub.py" &
ssh pi@controller "./zpub.py" &
sleep 4s
echo 'done!'

cd ~/git/active/cluster-hat/images

for client in 1 2
    do
     for i in {0..2}
       do
        cmd="pi@P${client}:p${client}-image${i}.jpg ."
        echo $cmd
        scp $cmd
       done
    done
echo 'copied'
