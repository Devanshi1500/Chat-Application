from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app=Flask(__name__)

app.config['SECRET_KEY']='mySecretKey'
socketio=SocketIO(app)

@app.route('/')
def index():
	return render_template("./chatApp.html")

@socketio.on('my event')
def handle_my_event(json):
	print("Received something" + str(json))
	socketio.emit('my response',json)





if __name__ == '__main__':
	socketio.run(app, debug=True)