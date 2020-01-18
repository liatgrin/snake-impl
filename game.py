class Game:

    def __init__(self, id):
        self.id = id

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y if isinstance(other, Coordinate) else False


class Snake:

    def __init__(self, id, name, health, body):
        self.id = id
        self.name = name
        self.health = health
        self.body = body
    
    @classmethod
    def from_json(cls, json_data: dict):
        body = list(map(Coordinate.from_json, json_data.pop('body')))
        return cls(**json_data, body=body)


class Board:

    def __init__(self, height, width, food, snakes):
        self.height = height
        self.width = width
        self.food = food
        self.snakes = snakes
    
    @classmethod
    def from_json(cls, json_data: dict):
        food = list(map(Coordinate.from_json, json_data.pop('food')))
        snakes = list(map(Snake.from_json, json_data.pop('snakes')))
        return cls(**json_data, food=food, snakes=snakes)