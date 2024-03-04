from flask import Flask, request
from flask_cors import CORS
import os
from upload_app import initialize_ui
app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def home():
    return "status ok \n <a href='/upload'>Upload</a>"

@app.route('/upload', methods=['GET'])
def upload():
    return initialize_ui(closing_message="application closed \n To retry click below link \n <a href='/upload'>Upload</a>")

@app.errorhandler(404)
def page_not_found():
    return "page not found", 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))