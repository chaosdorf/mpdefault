#!/usr/bin/env python2

uri = "http://voxsc1.somafm.com:8200"

import time
from mpd import MPDClient
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
        i = 10
        while i < 43:
            client.setvol(i)
            time.sleep(1)
            i = i+1
