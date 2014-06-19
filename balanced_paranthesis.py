#!/usr/bin/python
from stack import Stack
import sys

def check(str):
    s = Stack()
    balanced = True
    i = 0
    while i < len(str) and balanced:
        ch = str[i]
        i += 1
        if ch == '(':
            s.push(ch)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
    return balanced and s.isEmpty()
    
if __name__ == '__main__':
    strings = ['()', '((()()))', '(((()', '()))']
    for str in strings:
        if check(str):
            print('Balanced')
        else:
            print('Not balanced')