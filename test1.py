from flask import Flask
from flask import render_template

app=Flask(__name__)


@app.route('/')
def index():
   return render_template("SIGNATURE_VER_4_FILE_UPLOAD.html")


if __name__=="__main__":
   app.run()
