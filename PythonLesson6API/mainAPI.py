#Calling your API

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
print(response)

# for artworks in response:
#      print(response['title'])