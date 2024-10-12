#BUILDING APIS LESSON FOLLOW ALONG 1

# Will need to use flask
# Therefore, will need to install it first, the easiest way in Pycharm is to hover over flask
# then import when prompted
from flask import Flask,jsonify
from mock_database import characters #for exercise where I need to get info from this database
#to run this, right click then press 'Run Server' (one with green triangle) and not 'run in python console'!
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return jsonify("THIS IS ROOT")

@app.route("/name", methods=["GET"])
def meaningful_thing():
    return jsonify("Iman")


@app.route("/characters", methods=["GET"])
def get_characters():
    return jsonify(characters)

# @app.route("/characters/<int:an_id>", methods=["GET"])
# def get_character_by_id(an_id): #an_id in line above needs to match function parameter
#     print("ID IN SERVER IS: ", an_id)
#     return jsonify("WORKING ON IT....")

@app.route("/characters/<int:an_id>", methods=["GET"])
def get_character_by_id(an_id):
    char = [char for char in characters if char["id"] == an_id]
    return jsonify(char)

@app.route("/characters/<int:an_id>", methods=["DELETE"]) #The only method you can view in your browser is GET
def remove_character_by_id(an_id):
    #characters[:] splices the list, and removes anything that you do NOT want to delete 
    #characters[:] = [char for char in characters if char["id"] != an_id]
    char = [char for char in characters if char["id"] != an_id]
    print("Who is this?: ", char)
    return jsonify("WORKING ON IT...")

app.run(port=8000)    # server won't load in chrome (idk if that's the right terminology)
#so instead of port 5000 trying port 8000 and this seems to work
#for assignment, will expect to write results to file not to a server! therefore make another .py file for client
if __name__ == "__main__":
    app.run(debug=True)  # debug=True is only for development




