#BUILDING APIS LESSON FOLLOW ALONG 1

# Will need to use flask
# Therefore, will need to install it first, the easiest way in Pycharm is to hover over flask
# then import when prompted
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return jsonify("THIS IS ROOT")


if __name__ == "__main__":
    app.run(debug=True)