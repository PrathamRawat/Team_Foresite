# Pratham Rawat
# SoftDev1 pd1
# K<n> -- <Title/Topic/Summary>
# 2019-09-18   

from flask import Flask, render_template

app = Flask(__name__);

@app.route("/")
def whyTho():
   return render_template('')

if __name__ == "__main__":
    app.debug = True
    app.run()
