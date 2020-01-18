from flask import Flask, request
from game import Game, Board, Snake

import play

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def ping():
    return 'OK'

@app.route('/start', methods=['POST'])
def start():
    json = request.get_json()
    return play.start(Game.from_json(json['game']))

@app.route('/move', methods=['POST'])
def move():
    json = request.get_json()
    snake = Snake.from_json(json['you'])
    board = Board.from_json(json['board'])
    return play.move(snake, board, None)

@app.route('/end', methods=['POST'])
def end():
    play.end(request.get_json()['game']['id'])
    return 'OK'
