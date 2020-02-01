from game import Game, Board, Snake, Coordinate
from algorithm.closest_food_naive_algorithm import ClosestFoodNaiveAlgorithm
from algorithm.closest_food_with_obstacles_algorithm import ClosestFoodWithObstaclesAlgorithm

import random

games = {}

random_head = lambda: random.choice(["beluga", "bendr", "dead", "evil", "fang", "pixel", "regular", "safe", "sand-worm", "shades", "silly", "smile", "tongue"])
random_tail = lambda: random.choice(["block-bum", "bolt", "curled", "fat-rattle", "freckled", "hook", "pixel", "regular", "round-bum", "sharp", "skinny", "small-rattle"])
r = lambda: random.randint(0,255)
random_color = lambda: '#%02X%02X%02X' % (r(),r(),r())

alg = ClosestFoodWithObstaclesAlgorithm()

def start(game):
    # (if id in games)
    games[game.id] = game
    return {'color': random_color(),
        'headType': random_head(),
        'tailType': random_tail()
    }

def end(game_id):
    # games.pop(game_id)
    return

def move(snake, board, game):
    head = snake.body[0]
    return {'move': alg.next_move(head, board)}
    
