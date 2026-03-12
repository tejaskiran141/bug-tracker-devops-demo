from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_bugs():
    try:
        with open("bugs.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_bugs(bugs):
    with open("bugs.json", "w") as f:
        json.dump(bugs, f)

@app.route("/")
def home():
    return "Bug Tracker DevOps Demo Running"

@app.route("/bugs", methods=["GET"])
def get_bugs():
    bugs = load_bugs()
    return jsonify(bugs)

@app.route("/bugs", methods=["POST"])
def add_bug():
    bugs = load_bugs()
    data = request.json

    new_bug = {
        "id": len(bugs) + 1,
        "title": data["title"],
        "status": "open"
    }

    bugs.append(new_bug)
    save_bugs(bugs)

    return jsonify(new_bug)

@app.route("/bugs/<int:bug_id>/resolve", methods=["PUT"])
def resolve_bug(bug_id):
    bugs = load_bugs()

    for bug in bugs:
        if bug["id"] == bug_id:
            bug["status"] = "resolved"

    save_bugs(bugs)

    return jsonify({"message": "Bug resolved"})

if __name__ == "__main__":

    app.run(debug=True)
