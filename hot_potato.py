#!/usr/bin/python
from queue import Queue

def play(names, num):
    """
    A simulation of the hot-potato game
    names: names of all players
    num: simulation pauses after num transfers
    """
    q = Queue()
    i = 0
    # add everyone to the queue
    for name in names:
        q.enqueue(name)
    # start playing, stop with one winner
    while q.size() > 1:
        if i < num:
            q.enqueue(q.dequeue())  # circle through the players
            i += 1
        else:
            i = 0  # reset i
            q.dequeue()  # permanently remove this player
    return q.dequeue()

print(play(["Bill","David","Susan","Jane","Kent","Brad"],7))
            