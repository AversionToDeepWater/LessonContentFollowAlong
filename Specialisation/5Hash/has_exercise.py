"""
Let's create our own basic Hashing Algorithm that we can use
to obfuscate messages!

We'll only be hashing strings of alphanumeric input.

Your hash function should use ord() and chr() to find the
unicode values.

You should do something to the string, or the converted values
that counts as your secret for the encoding.

Make sure you create a function that encodes your message, and
one to decode your encoded messages!

"""

def hash_algorithm(message:str):
    encoded_list = [] #list of integers in list
    for i, char in enumerate(message): #enumerate gives tuple of (index, char)
        if i % 2 == 0:
            encoded_list.append(ord(char)) #adds integers to list
        else:
            encoded_list.append(ord(char) + 1 )
    return encoded_list

def unhash_alg(encoded:list):
    decoded = []
    for x in encoded:
        #have to use encoded.index(x) as I have a list on integers!
        if encoded.index(x) % 2 == 0:
        # Dependent on the *index* being divisible by 2 not the numerical value itself being divisible by 2
            decoded.append(chr(x))
        else:
            decoded.append(chr(x-1))
    return decoded


print(hash_algorithm('Hello World'))
hello_hash = [72, 102, 108, 109, 111, 33, 87, 112, 114, 109, 100]

print(unhash_alg((hello_hash)))