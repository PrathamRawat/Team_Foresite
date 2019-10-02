# Jesse Chen & Pratham Rawat
# SoftDev1 pd1
# K15 -- ?
# 2019-10-02

from flask import Flask, render_template

app = Flask(__name__);

@app.route("/")
def whyTho():
   return render_template('')

if __name__ == "__main__":
    app.debug = True
    app.run()
