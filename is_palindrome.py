
def removeWhite(s):
    return ''.join(s.split())

def isPal(s):
    # base case
    if len(s) <= 1:
        return True
    else:
        # check
        if s[0] != s[-1]:
            return False
        else:
            # make progress towards base case
            return isPal(s[1:-1])

