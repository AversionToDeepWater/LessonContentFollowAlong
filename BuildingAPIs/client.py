import requests
#for this to work with server.py, server.py needs to be running

#BETTER TO WRITE THIS AS A FUNCTION!!!
# endpoint = "http://127.0.0.1:8000/characters"
#
# data = requests.get(endpoint).json()
#
# print("Client says: ", data) #will print to python console

def get_root():
    endpoint = "http://127.0.0.1:8000"
    data = requests.get(endpoint).json()
    return data

#to split screen, right click an active open .py file and press 'split right'

#for assignment, will need a def run() function
def get_characters(): #ADVANCED - can have the root (e.g. /characters) as an input to the function
    endpoint = "http://127.0.0.1:8000/characters"
    data = requests.get(endpoint).json()
    return("Client says: ", data)
#in terminal, you will have a server tab and a client tab. You need to the server tab to ne up for this to work

def run():
    print(get_root())
    print(get_characters())

#ONLY RUN FUNCTIONS AFTER IF NAME == MAIN!! Otherwise, very bad for imports
if __name__ == "__main__":
    run() #run function will need to be here for assignment!!




