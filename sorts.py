#!/usr/bin/python

def bubble(a_list):
    """
    Sorts a list using short-bubble sort
    O(N^2) compares and O(N^2) exchanges
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

def selection(a_list):
    """
    Sorts a list using selection sort
    """
    # find minimum and put it in position
    N = len(a_list)
    for i in range(N):
        min = i
        for j in range(i+1, N):
            if a_list[j] < a_list[min]:
                min = j
        a_list[i], a_list[min] = a_list[min], a_list[i]
    