class Player:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.text = "P"

    def print(self):
        print(self.x,self.y)

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def move_to(self,x,y):
        self.x = x
        self.y = y

    def cal_next(self,dx,dy):
        return [self.x + dx,self.y + dy]

    def match(self,x,y):
        if self.x == x and self.y == y:
            return True

# player = Player(3,5)  # where is self? player is self now! and Player is __init_ : Hàm Khởi Tạo
# player.print()
# player.move(1,0)
# player.print()
# player.move_to(2,3)
# player.print()
# player.cal_next(1,2)
# print(player.cal_next(1,1))
#
#
# player2 = Player(2,7)
# player2.print()
# player2.move_to(10,2)
# player2.move(2,3)
# player2.print()
# player2.cal_next(1,2)
# print(player2.cal_next(1,2))