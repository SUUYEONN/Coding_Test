import re

def solution(my_string):
    p = re.compile('[a-zA-Z]+')
    m = p.findall(my_string)
    return m

"""
def solution(my_string):
    return my_string.split()
"""