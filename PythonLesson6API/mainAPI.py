#Calling your API
from pprint import pprint

#First you need to import requests library, otherwise you can't call your API.
#All imports and requests should be at the top of your code
import requests
#You then need to specify your endpoint, i.e., the https for your API
#Note, you can first call your API on Insomnia and analyse the data structure there
endpoint = "https://api.artic.edu/api/v1/artworks?fields=id,title,artist_display,date_display,main_reference_number,description,alt_text,short_description"
# https://api.artic.edu/api/v1/artworks?fields=id,title,artist_display,date_display,main_reference_number,description,alt_text,short_description
#https://api.artic.edu/api/v1/artworks
#Call requests library, to use a special get method to get data from endpoint. Save to respomse
response = requests.get(endpoint).json()
#For the actual data, which will come from the internet as a JSON file
#For Python to understand this, you need to use inbuilt JSON function to import JSON package in Python script
#data = response.json()
#print(response)

total_artworks = response['pagination']['total'] #total no of artworks

#Figuring out what data from JSON data I want
title = response['data'][0]['title'] #title of the first artwork - data is a list, [0] for first item in list, 'title' is key
description = response['data'][0]['description'] #description of first artwork, too long
short_description = response['data'][0]['short_description'] #short description of first artwork which I prefer to use
artist_display = response['data'][0]['artist_display'] #Artist name, and info
# print(artist_display)

def get_description(response:str, i:int): #get short description of artwork based on lucky no?
    short_description = response['data'][i]['short_description']
    return short_description

def get_artist_info(response:str): #returns list of titles and artist info from API
    for item in response['data']:
        print(item['title'], item['artist_display'])
    return

get_artist_info(response)




print(get_description(response,0))

# art = response[0]['title']
#
# print(art)