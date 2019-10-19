from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

@app.route("/")
def index():
	return "Welcome to this Flask application"

data = {'name':'Varun',}


@app.route("/api/hello",methods=['GET'])
def api_hello():
    return jsonify(data)

if __name__=='__main__':
	app.run()
