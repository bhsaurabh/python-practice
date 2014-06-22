#!/usr/bin/python

def bubble(a_list):
    """
    Sorts a list using bubble sort
    """
    for pass_number in range(len(a_list)-1, 0, -1):
        # pass number approach is more efficient, as with every iteration
        # largest element is in position
        for i in range(pass_number):
            if a_list[i] > a_list[i+1]:
                # exchange
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                