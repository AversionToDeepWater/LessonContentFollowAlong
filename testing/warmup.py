# take a string and add dash between each letter

string = "Sally"

def string_split(s:str) -> str: # -> str means function returns a string and everyone should expect a string
    x = s.replace('', '-') #also adds '-' to start and end of word
    return x

def other_string_split(s:str) -> str:
    list_s = list(s)
    join_s = "-".join(list_s) #doesn't add '-' to start and end of word
    return join_s

print(other_string_split(string))