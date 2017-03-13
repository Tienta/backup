class GameView:
    def __init__(self,image): # not have screen because you can change the screen you draw in
        self.image = image
        self.width = 32
        self.heigh = 32

    def draw(self, screen, game_model):
        x = game_model.x * self.width
        y = game_model.y * self.heigh
        #width = self.width
        #height = self.heigh
        screen.blit(self.image,(x, y))