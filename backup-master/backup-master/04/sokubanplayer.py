class Player:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.text = "P "

    def move(self,dx,dy):
        self.x += dx
        self.y += dy


    def calc_move(self,dx,dy):
        return [self.x + dx, self.y + dy]

    def match(self,x,y):
        if self.x == x and self.y == y:
            return True
    def check_move(self,dx,dy):
        next_px = self.x + dx
        next_py = self.y + dy
        return [next_px,next_py]