#!/usr/bin/python
from deque import Deque
import sys

# this is extraordinarily complex (O(n^2))
# normally palindrome checking is O(n), this is just a use of the Deck datastructure
def is_palindrome(str):
    q = Deque()
    for ch in list(str):
        q.addFront(ch)  # insert from front of deque as this is O(1)
    
    palindrome = True
    while q.size() > 1 and palindrome:
        # if even, it will be 0; else it will be 1
        front = q.removeFront()  # O(1)
        rear = q.removeRear()  # Bingo! O(n)  <--- This is bad
        if front != rear:
            palindrome = False
    return palindrome


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('Not enough args\n')
    else:
        for str in sys.argv[1:]:
            print(is_palindrome(str))