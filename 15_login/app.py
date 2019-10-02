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
	except:
		return render_template('start.html')

@app.route("/login")
def logIn():
	return 0

if __name__ == "__main__":
    app.debug = True
    app.run()
