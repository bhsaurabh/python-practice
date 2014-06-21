#!/usr./bin/python

def reverse(s):
    """
    reverses a string (uses recursion)
    """
    if len(s) <= 1:  # base case
        return(s)
    else:
        # move towards base case
        # make some progress towards solution
        return(s[-1] + reverse(s[:-1]))
