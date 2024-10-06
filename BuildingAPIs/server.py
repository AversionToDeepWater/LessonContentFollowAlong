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

app.run(port=8000)    # server won't load in chrome (idk if that's the right terminology)
#so instead of port 5000 trying port 8000 and this seems to work
#for assignment, will expect to write results to file not to a server! therefore make another .py file for client
if __name__ == "__main__":
    app.run(debug=True)



