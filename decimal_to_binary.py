#!/usr/bin/python
import sys
from stack import Stack

def convert(num):
    # works only for positive numbers
    s = Stack()
    while num > 0:
        s.push(num % 2)
        num = num // 2
    binary = 0
    power = s.size() - 1
    while not s.isEmpty():
        binary += s.pop() * 10**power
        power -= 1
    return binary

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('Not enough args\n')
    for number in sys.argv[1:]:
        print(convert(int(number)))