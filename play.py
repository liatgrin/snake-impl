from game import Game, Board, Snake, Coordinate

import random

games = {}

random_head = lambda: random.choice(["beluga", "bendr", "dead", "evil", "fang", "pixel", "regular", "safe", "sand-worm", "shades", "silly", "smile", "tongue"])
random_tail = lambda: random.choice(["block-bum", "bolt", "curled", "fat-rattle", "freckled", "hook", "pixel", "regular", "round-bum", "sharp", "skinny", "small-rattle"])
r = lambda: random.randint(0,255)
random_color = lambda: '#%02X%02X%02X' % (r(),r(),r())

def start(game):
    # (if id in games)
    games[game.id] = game
    return {'color': random_color(),
        'headType': random_head(),
        'tailType': random_tail()
    }

def end(game_id):
    games.pop(game_id)

up = lambda c: Coordinate(c.x, c.y - 1)
down = lambda c: Coordinate(c.x, c.y + 1)
left = lambda c: Coordinate(c.x - 1, c.y)
right = lambda c: Coordinate(c.x + 1, c.y)

def move(snake, board, game):
    head = snake.body[0]
    possible_moves = {
        'right': right(head),
        'left': left(head),
        'down': down(head),
        'up': up(head)
    }
    possible_moves = {move: coord for move, coord in possible_moves.items() if is_valid_coordinate(coord, board)}
    closest_food = min(board.food, key=lambda food: abs(food.x - head.x) + abs(food.y - head.y))
    best_move = min(possible_moves.keys(), key=lambda move: abs(closest_food.x - possible_moves[move].x) + abs(closest_food.y - possible_moves[move].y))
    return {'move': best_move}
    
def is_valid_coordinate(coord, board):
    if coord.x < 0 or coord.y < 0 or coord.x >= board.width or coord.y >= board.height:
        # out of bounds
        return False
    
    for snake in board.snakes:
        for c in snake.body:
            if coord == c:
                # collision
                return False
    return True
