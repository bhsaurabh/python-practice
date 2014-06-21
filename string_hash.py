#!/usr/bin/python

def hash(string, table_size):
    """
    A hash function for strings. 
    Assigns weights to characters to remedy anagrams
    having same hash values
    """
    sum = 0
    weight = 1
    for i in range(len(string)):
        ch = ord(string[i])
        sum += ch*weight
        weight += 1
    return sum % table_size