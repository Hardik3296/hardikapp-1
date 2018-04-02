from flask import Flask 
import os

app = Flask(__name__)
port = int(os.getenv("PORT"))
@app.route('/')
def hello_world():
	return 'Welcome'

if __name__ == '__main__':
	#port = 12345
	app.run(host='0.0.0.0',port=port)
	#app.run(host='127.0.0.1',port=port)