#!/usr/bin/python

def search(a_list, item):
    """
    Search for an item in a list
    O(N)
    
    Args:
        a_list: List to search in
        item: Item to search for
    
    Returns:
        True, if item is found; False otherwise
    """
    for el in a_list:
        if el == item:
            return True
    return False

def ordered_search(a_list, item):
    """
    Sequential search on an ordered list
    O(N)
    """
    for el in a_list:
        if el == item:
            return True  # element found!
        elif el > item:
            # no more items need to be compared and the element is not in the list
            break
    return False

if __name__ == '__main__':
    print(search([1,2,3,4,5,6,7,8,9], 7))
    print(search([1,2,3,4,5,6,7,8,9], 0))
    print(ordered_search([1,2,3,4,5,6,7,8,9], 7))
    print(ordered_search([1,2,3,4,5,6,7,8,9], 10))
    print(ordered_search([1,2,3,4,5,6,7,8,9], -1))