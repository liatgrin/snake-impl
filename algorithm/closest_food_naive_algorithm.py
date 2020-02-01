from game import Coordinate, Board

up = lambda c: Coordinate(c.x, c.y - 1)
down = lambda c: Coordinate(c.x, c.y + 1)
left = lambda c: Coordinate(c.x - 1, c.y)
right = lambda c: Coordinate(c.x + 1, c.y)

class ClosestFoodNaiveAlgorithm:

    def next_move(self, head, board):
        possible_moves = {
            'right': right(head),
            'left': left(head),
            'down': down(head),
            'up': up(head)
        }
        possible_moves = {move: coord for move, coord in possible_moves.items() if self.is_valid_coordinate(coord, board)}
        closest_food = min(board.food, key=lambda food: abs(food.x - head.x) + abs(food.y - head.y))
        best_move = min(possible_moves.keys(), key=lambda move: abs(closest_food.x - possible_moves[move].x) + abs(closest_food.y - possible_moves[move].y))
        return best_move

    def is_valid_coordinate(self, coord, board):
        if coord.x < 0 or coord.y < 0 or coord.x >= board.width or coord.y >= board.height:
            # out of bounds
            return False
    
        for snake in board.snakes:
            for c in snake.body:
                if coord == c:
                    # collision
                    return False
        return True