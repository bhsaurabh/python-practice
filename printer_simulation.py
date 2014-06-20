#!/usr/bin/python

from printer import Printer
from task import Task
from queue import Queue
import random

def simulation(num_seconds, pages_per_minute):
    my_printer = Printer(pages_per_minute)
    printing_queue = Queue()  # queue of all printing tasks
    wait_times = []  # tracks waiting time for each task, later used for getting mean
    
    for current_second in range(num_seconds):
        # 20 pages per hour => 1 page every 180 seconds
        # generate a random number in 1, 180; and create a task if num is 180
        if new_task_created():
            # create a new task
            new_task = Task(current_second)
            # pages are set in randomly for simulation within task object
            printing_queue.enqueue(new_task)
        
        # start a new task on the printer, if it is free
        if not my_printer.busy() and not printing_queue.isEmpty():
            next_task = printing_queue.dequeue()
            # calculate waiting time for current task
            wait_times.append(next_task.waitTime(current_second))
            # start this task
            my_printer.startNext(next_task)
        
        # update printer's clock
        my_printer.tick()
    
    # compute average wait time
    avg_wait_time = (sum(wait_times) * 1.0) / len(wait_times)
    print("Average Wait %6.2f secs %3d tasks remaining."%(avg_wait_time, printing_queue.size()))

def new_task_created():
    r = random.randrange(1, 181)
    return r == 180

if __name__ == '__main__':
    simulation(3600, 5)