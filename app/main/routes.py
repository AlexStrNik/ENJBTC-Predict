from flask import session, redirect, url_for, render_template, request
from flask_socketio import emit, join_room, leave_room
from . import main
import json
from .. import socketio

room = 'QWERTY'
prices = []


@main.route('/getPrice')
def get_price():
    return json.dumps(prices)


@main.route('/', methods=['POST'])
def post():
    print(request.json)
    join_room(room)
    pass
    emit('message', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@main.route('/', methods=['GET'])
def index():
    """Login form to enter a room."""
    return render_template('index.html')
