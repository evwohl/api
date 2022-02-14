from flask import Flask, request
import ids
# create the Flask app
app = Flask(__name__)


def check(hwid):
    try:
        with open('hwid.txt') as temp_f:
            datafile = temp_f.readlines()
        for line in datafile:
            if hwid in line:
                return True # The string is found
        return False  # The string does not exist in the fil
    except:
        return False
def keyValid(key):
    try:
        if key in ids.idlist:
            return True
        return False  # The string does not exist in the fil
    except:
        return False

@app.route('/isAuthorized')
def login():
    try:
        hwid = request.args.get('hwid')
        print(hwid)
        if check(hwid):
            return "True"
        return "False"
    except Exception as e:
        return f"ERROR: {e}"
@app.route('/authorize')
def auth():
    try:
        hwid = request.args.get('hwid')
        auth = request.args.get('auth')
        print(hwid)
        if keyValid(auth):
            ids.idlist = ids.idlist.replace(auth, "")
            f = open("hwid.txt", "a")
            f.write(f"{hwid}\n")
            f.close()
            f = open("used.txt", "a")
            f.write(f"{auth}\n")
            f.close()
            return "True"
        return "False"
    except Exception as e:
        return f"ERROR: {e}"

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)