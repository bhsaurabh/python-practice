#!/usr/bin/python

import random

class Task(object):
    def __init__(self,time):
        self.timestamp = time  # every printing task has a timestamp
        self.pages = random.randrange(1,21)  # simulation variable (random number in [1, 20])

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp