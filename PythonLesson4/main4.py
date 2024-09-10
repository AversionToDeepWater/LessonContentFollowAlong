"""
 Print the values of name, post_code and street_number from the dictionary in a
 readable way
"""
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

'''
Extension: Print the values of longitude and latitude from the inner dictionary 

'''

print(f"Name:{place['name']} \n Post Code: {place['post_code']} \n Street Number: {place['street_number']}")