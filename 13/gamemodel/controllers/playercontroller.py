import pygame
from views.gameviews import GameView
from models.gamemodel import GameModel


class PlayerController:
    def __init__(self,game_model,game_view):
        self.game_model = game_model
        self.game_view = game_view

    def draw(self,screen):
        self.game_view.draw(screen, self.game_model)

    def process(self,key):
        if key == pygame.K_DOWN:
            self.game_model.move(0,1)
        if key == pygame.K_UP:
            self.game_model.move(0,-1)
        if key == pygame.K_LEFT:
            self.game_model.move(-1,0)
        if key == pygame.K_RIGHT:
            self.game_model.move(1,0)

# factory --> import
def create_playercontroller(x,y):
    game_model = GameModel(x,y)
    game_view = GameView(pygame.image.load("views/images/image-1.jpg"))
    player_controller = PlayerController(game_model,game_view)
    return player_controller