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
        if ch in '{[(':
            s.push(ch)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, ch):
                    balanced = False
    return balanced and s.isEmpty()

def matches(open, close):
    openers = '{[('
    closers = '}])'
    return openers.index(open) == closers.index(close)
    
if __name__ == '__main__':
    strings = ['[()]', '[({}[(()())])]', '(((()', '()))']
    for str in strings:
        if check(str):
            print('Balanced')
        else:
            print('Not balanced')