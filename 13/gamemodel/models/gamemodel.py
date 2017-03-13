class GameModel : # class name
    def __init__(self, x, y): # You can add  width, height
        self.x = x
        self.y = y
# move object
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# return next position
    def calc_next_pos(self, dx, dy):
        return [self.x + dx, self.y + dy]

#check working
    def print(self):
        print("x = {0}, y = {1}".format(self.x, self.y))