#!/usr/bin/env python2

uri = "http://voxsc1.somafm.com:8200"

import time
from mpd import MPDClient


def serve():
    client = MPDClient()
    client.connect("localhost", 6600)

    while True:
        time.sleep(5)
        if len(client.playlist()) == 0:
            client.addid(uri)
            client.consume(1)
            client.crossfade(0)
            client.random(0)
            client.repeat(0)
            client.single(0)
            client.play()
            time.sleep(1)
            
            for i in range(10, 43):
                client.setvol(i)
                time.sleep(0.5)

while True:
    try:
        serve()
    except Exception as ex:
        print ex
        time.sleep(6.66)

