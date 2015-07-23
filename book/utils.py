__author__ = 'letsoon'

def is_empty(string):
    if string:
        return string.replace(' ', '') == ''
    else:
        return True
