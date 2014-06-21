#!/usr/bin/python

def binary_search(a_list, item):
    """
    Perform binary search to locate an item in a list
    
    Args:
        a_list: A sorted list, to search for the element
        item: Element to be searched for
    
    Returns:
        True, if item is found; False otherwise
    """
    lo, hi = 0, len(a_list)-1
    while hi >= lo:
        mid = lo + (hi - lo) / 2
        if a_list[mid] > item:
            # scan lower half
            hi = mid - 1
        elif a_list[mid] < item:
            # scan upper half
            lo = mid + 1
        else:
            # Found element
            return mid
    # not found, return -1
    return -1

if __name__ == '__main__':
    print(binary_search([1,2,3,4,5,6,7,8,9], 7))
    print(binary_search([1,2,3,4,5,6,7,8,9], 70))