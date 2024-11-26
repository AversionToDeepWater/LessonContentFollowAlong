###################################################################
# 2. First unique character

# Given an input string, find the first non-repeating character

s = 'aabccbdcbe'

def FirstUniqueChar(string:str) -> str:
    for s in string:
        if string.count(s) == 1:
            return s

print(FirstUniqueChar(s))
