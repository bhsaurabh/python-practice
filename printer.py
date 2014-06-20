#!/usr/bin/python

class Printer(object):
    def __init__(self, ppm):
        self.pagerate = ppm  # assign pagerate to the printer
        self.currentTask = None  # keep track of current task
        self.timeRemaining = 0  # time remaining to complete this task

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1  # no need to wait a second to simulate it
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newTask):
        self.currentTask = newTask  # start new task
        self.timeRemaining = newTask.getPages() * 60/self.pagerate  # estimate time remaining
