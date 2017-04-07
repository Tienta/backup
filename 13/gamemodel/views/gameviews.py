class GameView:
    def __init__(self,image): # not have screen because you can change the screen you draw in
        self.image = image
        self.width = 32
        self.height = 32

    def draw(self, screen, game_model):
        x = game_model.x * self.width
        y = game_model.y * self.height
        #width = self.width
        #height = self.height
        screen.blit(self.image,(x, y))