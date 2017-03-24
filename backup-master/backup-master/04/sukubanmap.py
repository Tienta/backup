from sokubanplayer import Player
from sokubanboxes import Box
from sokubangate import Gate

class Map:

    def __init__(self,height=0,width=0):
        self.height = height
        self.width = width
        self.player = Player(2,0)
        self.box = Box(1,2)
        self.gate = Gate(3,3)

    def print_map(self):
        for y in range (self.height):
            for x in range(self.width):
                if self.player.match(x,y):
                    print(self.player.text, end='')
                elif self.box.match(x,y):
                    print(self.box.text, end='')
                elif self.gate.match(x,y):
                    print(self.gate.text, end='')
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

        if self.in_map(self.player.calc_move(dx,dy)[0],self.player.calc_move(dx,dy)[1]):
            if self.collide(dx,dy):
                if self.in_map(self.box.calc_move(dx,dy)[0],self.box.calc_move(dx,dy)[1]) :
                    self.move_player(dx,dy)
                    self.move_box(dx,dy)
            elif not self.collide(dx,dy):
                self.move_player(dx,dy)


        self.player.move(dx,dy)
    def collide(self,dx,dy):
        if self.player.calc_move(dx,dy)[0] == self.box.x and self.player.calc_move(dx,dy)[1] == self.box.y:
            return True
        return False
    def in_map(self,x,y):
        if x < 0 and x > self.width -1 and y < 0 and y > self.height -1:
            return False
        return True

    def check_win(self):
        if self.box.x == self.gate.x and self.box.y == self.gate.y:
            return True

    def loop(self):
        while True:
            self.print_map()
            if self.check_win()==True:
                print("Win")
                break
            move = input("Your move: W,A,S,D ")
            self.process_input(move)




    # def in_map(self,dx,dy):
        # if map.move_player(dx,dy)< 0 :

map = Map(5,5)
map.loop()
