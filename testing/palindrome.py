

def check_palindrome(s:str) -> bool:
    n = s.lower()
    if n == n[::-1]: #[::-1] reverses a string, slice end of string one step backwards
        return True
    else:
        return False

print(check_palindrome(""))
