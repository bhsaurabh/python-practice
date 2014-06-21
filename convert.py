#!/usr/bin/python
import sys

converted = []  # stores the converted string as a list

def convert(base, num):
    """
    Converts a number in base 10 to any other base
    """
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


def convert_aliter(n,base):
    """
    An alternative way to convert from one base to another
    """
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return convert_aliter(n//base, base) + convert_string[n%base]

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
        