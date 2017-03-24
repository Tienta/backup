class Gate:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.text = "o "

    def match(self, x, y):
        if self.x == x and self.y == y:
            return True
