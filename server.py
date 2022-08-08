from flask import Flask
from flask import request
import json
import os

os.system('cls||clear')

if not os.path.exists("games"):
    os.mkdir("games")

app = Flask(__name__)


@app.route("/<session_id>")
def session(session_id):
    pass


@app.route('/create', methods=['POST'])
def create():
    jsondata = request.get_json()
    session_id = jsondata['session_id']

    # check if the session_id is already in use
    if os.path.exists(rf".\\games\\{session_id}.json"):
        return json.dumps({"status": "error", "message": "Session ID already in use"})

    # create the session
    with open(rf".\\games\\{session_id}.json", "w") as f:
        f.write(json.dumps({"status": "ok", "message": "Session created"}))
    return json.dumps({"status": "ok", "message": "Session created"})


@ app.route('/join', methods=['POST'])
def join(session_id):
    jsondata = request.get_json()
    session_id = jsondata['session_id']
    # check if the session_id is valid
    if not session_id.isdigit():
        return json.dumps({"status": "error", "message": "Invalid session ID"})

    # check if the session_id is already in use
    if not os.path.exists(rf".\\games\\{session_id}.json"):
        return json.dumps({"status": "error", "message": "Session ID not found"})

    # join the session
    with open(rf".\\games\\{session_id}.json", "w") as f:
        f.write(json.dumps({"status": "ok", "message": "Session joined"}))
    return json.dumps({"status": "ok", "message": "Session joined"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
