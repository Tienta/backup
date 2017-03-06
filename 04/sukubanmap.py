from sokubanplayer import Player
from sokubanboxes import Box
from sokubangate import Gate
from sokubanwalls import Walls
class Map:

    def __init__(self,height=0,width=0):
        self.height = height
        self.width = width
        self.player = Player(2,0)
        self.box = Box(1,2)
        self.gate = Gate(3,3)
        self.walls = Walls(2,4)

    def print_map(self):
        for y in range (self.height):
            for x in range(self.width):
                if self.player.match(x,y):
                    print(self.player.text, end=' ')
                elif self.box.match(x,y):
                    print(self.box.text, end=' ')
                elif self.gate.match(x,y):
                    print(self.gate.text, end=' ')
                elif self.walls.match(x,y):
                    print(self.walls.text, end=' ')
                else:
                    print("_ ", end='')
            print()

    def move_player(self,dx, dy):
        return self.player.move(dx,dy)

    def move_box(self,dx,dy):
        self.box.move(dx,dy)

    def process_input(self,move):
        direction = move.upper()
        dx,dy = 0,0
        if direction == "W":
            dx,dy = 0,-1
        elif direction == "S":
            dx,dy = 0,1
        elif direction == "D":
            dx,dy = 1,0
        elif direction == "A":
            dx,dy = -1,0

        self.player.move(dx,dy)

    def in_map(self,dx,dy):
        if self.player.move(dx,dy) < 0 or self.move_player(dx,dy) > self.player.move(dx,dy) > 4 or self.box.move(dx,dy) < 0 and self.box.move(dx,dy)> 4 or
            return False
        return True

    def loop(self):
        while True:
            self.print_map()
            move = input("Your move: W,A,S,D ")
            self.in_map(dx, dy)
            self.process_input(move)


    # def in_map(self,dx,dy):
        # if map.move_player(dx,dy)< 0 :

map = Map(5,5)
map.loop()
