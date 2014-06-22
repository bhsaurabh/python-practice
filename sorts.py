#!/usr/bin/python

def bubble(a_list):
    """
    Sorts a list using short-bubble sort
    """
    exchanges = True
    pass_number = len(a_list) - 1  # number of passes
    while pass_number > 0 and exchanges:
        exchanges = False  # proceed only if there are exchanges made
        for i in range(pass_number):
            if a_list[i] > a_list[i+1]:
                exchanges = True
                # exchange
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]