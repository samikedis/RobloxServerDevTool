'''
    Roblox developer tool for roblox server management and statistics 
'''
from flask import Flask

_version = "0.00.01"

app = Flask(__name__)

@app.route("/")
def main():
    return "Currently running version {_version} of Rbx Server Tool & Analytics"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")