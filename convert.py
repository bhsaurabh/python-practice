#!/usr/bin/python
import sys

converted = []  # stores the converted string as a list

def convert(base, num):
    reference = '0123456789ABCDEF'
    if num < base:
        # base case
        ch = reference[num]
    else:
        # recursion
        rem = num % base
        ch = reference[rem]
        num = num // base
        convert(base, num)
    # now append to converted list
    converted.append(ch)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('Not enough args. Usage: ./convert.py <base> <num1> <num2> ...\n')
    else:
        base = int(sys.argv[1])
        num_list = sys.argv[2:]
        for num in num_list:
            converted = []  # reset this list every time
            convert(base, int(num))
            print(''.join(converted))
        