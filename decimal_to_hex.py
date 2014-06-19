#!/usr/bin/python
import sys
from stack import Stack

def convert(num):
    # works only for positive numbers
    digits = '0123456789ABCDEF'
    s = Stack()
    while num > 0:
        s.push(num % 16)
        num = num // 16
    hex_value = []  # dont use a string here as repeated addition to it is quadratic
    while not s.isEmpty():
        hex_value.append(digits[s.pop()])
    return ''.join(hex_value)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('Not enough args\n')
    for number in sys.argv[1:]:
        print(convert(int(number)))