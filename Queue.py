from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def printQueue(self):
        string = ''
        for item in self.queue:
            string += ("--> " + str(item))
        return string