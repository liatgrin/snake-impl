from game import Coordinate

up = lambda c: Coordinate(c.x, c.y - 1)
down = lambda c: Coordinate(c.x, c.y + 1)
left = lambda c: Coordinate(c.x - 1, c.y)
right = lambda c: Coordinate(c.x + 1, c.y)

class Node:

    def __init__(self, coord, distance, parent=None, direction=None):
        self.coord = coord
        self.direction = direction
        self.distance = distance
        self.parent = parent


class ClosestFoodWithObstaclesAlgorithm:

    def next_move(self, head, board):
        node = self.build_path(head, board)
        while node.parent.coord != head:
            node = node.parent
        return node.direction
    
    def build_path(self, head, board):
        current_layer = [Node(head, 0)]
        marked_coords = [head]

        while True:
            new_layer = []
            for node in current_layer:
                if node.coord in board.food:
                    return node
                adjacent_nodes = self.get_adjacent_nodes(node)
                new_layer.extend(node for node in adjacent_nodes if self.is_valid_coordinate(node.coord, board) and node.coord not in marked_coords)
                marked_coords.extend(node.coord for node in adjacent_nodes)
            if not new_layer:
                return None
            current_layer = new_layer
    
    def get_adjacent_nodes(self, node):
        distance = node.distance + 1
        coord = node.coord
        return [
            Node(up(coord), distance, node, 'up'),
            Node(down(coord), distance, node, 'down'),
            Node(left(coord), distance, node, 'left'),
            Node(right(coord), distance, node, 'right')
        ]
    
    # def _build_path(self, root):
    #     path = [(root, 0)]
    #     distance = 1
    #     current_coords = [root]
        
    #     should_continue = True
    #     while should_continue:
    #         next_coords = []
    #         for coord in current_coords:
    #             if coord in self.board.food:
    #                 should_continue = False

    #             path_coords = list(zip(*path))[0]
    #             adjacent_coords = self.get_adjacent_cells(coord)
    #             adjacent_coords = [c for c in adjacent_coords if self.is_valid_coordinate(c, self.board) and c not in path_coords]

    #             next_coords.append(next_coords)
    #             path.append(zip(next_coords, [distance] * 4))
            
    #         current_coords = next_coords
    #         distance += 1

    # def get_adjacent_cells(self, coord):
    #     return [up(coord), down(coord), left(coord), right(coord)]
    
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
