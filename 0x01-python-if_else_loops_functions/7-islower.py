#!/usr/bin/python3
def islower(c):
    """Checks for lowercase

    Args:
        c: a single character argument

    Returns:
        True: if c is lowercase
        False: if c is not lowercase
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
