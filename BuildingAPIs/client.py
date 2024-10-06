import requests
#for this to work with server.py, server.py needs to be running

#BETTER TO WRITE THIS AS A FUNCTION!!!
# endpoint = "http://127.0.0.1:8000/characters"
#
# data = requests.get(endpoint).json()
#
# print("Client says: ", data) #will print to python console

#to split screen, right click an active open .py file and press 'split right'

#for assignment, will need a def run() function
def get_characters(): #ADVANCED - can have the root (e.g. /characters) as an input to the function
    endpoint = "http://127.0.0.1:8000/characters"
    data = requests.get(endpoint).json()
    return("Client says: ", data)

#ONLY RUN FUNCTIONS AFTER IF NAME == MAIN!! Otherwise, very bad for imports
if __name__ == "__main__":
    print(get_characters()) #run function will need to be here for assignment!!




