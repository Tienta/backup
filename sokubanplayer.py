class Player:
    def __init__(self,x=0,y=0):
        self.position = [{"x": x,"y": y}]
        self.text = "P "
    def move(self,dx,dy):
        self.position["x"] += dx
        self.position["y"] += dy

    def calc_move(self,dx,dy):
        self.position["x"] += dx
        self.position["y"] += dy
        return self.position