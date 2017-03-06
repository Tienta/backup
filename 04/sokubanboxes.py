class Box:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.text = "B"

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def match(self,x,y):
        if self.x == x and self.y == y:
            return True
