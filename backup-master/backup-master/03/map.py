from player import Player
class Map:
    def __init__(self,width, height):
        self.player = Player(1,1)
        self.width = width
        self.height = height
    def print(self):
        for y in range (self.width):
            for x in range(self.height):
                if self.player.match(x,y):
                    print(self.player.text, end=" ")
                else:
                    print("_ ", end="")
            print()
    def move_player(self,dx,dy):
        self.player.x += dx
        self.player.y += dy
    def process_input(self,move):
        direction = move.upper()
        dx,dy = 0,0
        if direction == "W":
            dx,dy = 0, -1
        elif direction == "S":
            dx, dy = 0, 1
        elif direction == "A":
            dx, dy = -1, 0
        elif direction == "D":
            dx, dy = 1, 0

        self.move_player(dx,dy)

    def loop(self):
        while True :
            self.print()
            move = input("Pick: W-S-D-A")
            self.process_input(move)


map = Map(5,5)
map.loop()
