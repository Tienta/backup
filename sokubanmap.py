from sokubanplayer import Player
from sokubanstuff import Boxes
from sokubanstuff import Walls
from sokubanstuff import Points


def check_match(list_dic, x, y):
    for dictionary in (list_dic):
        if dictionary["x"] == x and dictionary["y"] == y:
            return True

def check_in_map(obj,map_width,map_height):
    if  obj["x"] < 0 or obj["x"] >= map_width or obj["y"] < 0 or obj["y"] >= map_height:
        return False
    return True

def input_direction(player_choice):
    dx,dy = 0,0
    if player_choice == "W":
        dx,dy = 0, -1
    elif player_choice == "S":
        dx,dy = 0, 1
    elif player_choice == "A":
        dx,dy = -1, 0
    elif player_choice == "D":
        dx,dy = 1,0


class Map:
    def __init__(self,width,height):
        self.square = {"x": width, "y": height}
        self.player = Player()
        self.boxes = Boxes()
        self.points = Points()
        self.walls = Walls()

    def print_map(self):
        for y in range (self.square["y"]):
            for x in range (self.square["x"]):
                if check_match(self.player.position,x,y):
                    print(self.player.text,end='')
                elif check_match(self.boxes.position,x,y):
                    print(self.boxes.text,end='')
                elif check_match(self.points.position,x,y):
                    print(self.points.text,end='')
                elif check_match(self.walls.position,x,y):
                    print(self.walls.text,end='')
                else:
                    print("_ ", end='')
            print()

    def lauch(self):
        while True:
            choice = input("W-S-A-D: ").upper()
            input_direction(choice)

map = Map(6,6)
print(map.print_map())