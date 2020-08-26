import json
usr={}
def writeUsers(usr):
    with open("userkeys/users.json", "w+") as f: json.dump(usr, f)
def readUsers():
    try:
        with open("userkeys/users.json", "r") as f: return json.load(f)
    except FileNotFoundError:
        return {}
