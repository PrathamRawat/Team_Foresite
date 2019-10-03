# Jesse Chen & Pratham Rawat
# SoftDev1 pd1
# K15 -- ?
# 2019-10-02

from flask import Flask, render_template, session

app = Flask(__name__);

@app.route("/")
def whyTho():
    try:
        userData = request.cookies
        username = userData["username"]
        userpswd = userData["password"]
        return checkCredentials(username, userpswd)
    except:
        return render_template('start.html')

@app.route("/login", methods=['POST'])
def logIn():
    return render_template('start.html')

def checkCredentials(username, password):
    userData = open("data/accounts.csv");
    accountsDict = {}
    for line in userData:
        try:
            if(accountsDict[username] != password):
                print("Incorrect Password")
                return render_template("start.html", error = "Incorrect Password!")
        except: #Will run if the username does not exist in the Dictionary
            print("No username found!")
            return render_template("start.html", error = "Incorrect Username!")


if __name__ == "__main__":
    app.debug = True
    app.run()
