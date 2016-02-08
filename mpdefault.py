#!/usr/bin/env python2

import time
from mpd import MPDClient

host = "localhost"
port = 6600
uri = "http://ice1.somafm.com/spacestation-128.mp3"


def serve():
    client = MPDClient()
    client.connect(host, port)

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
            time.sleep(0.5)
            client.setvol(9)

            for i in range(10, 43):
                time.sleep(0.5)
                client.setvol(i)

while True:
    try:
        serve()
    except Exception as ex:
        print ex
        time.sleep(6.66)

