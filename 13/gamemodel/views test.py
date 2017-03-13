import pygame
from models.gamemodel import GameModel
from views.gameviews import GameView

pygame.init()
pygame.display.set_caption("Introduction to pygame")
screen = pygame.display.set_mode((400, 300))
done = False
BACK_GROUND = (148, 198, 153)

game_model = GameModel(5,6)
game_view = GameView(pygame.image.load("views/images/image-1.jpg"))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # test move of game model on views
            if event.key == pygame.K_LEFT:
                 game_model.move(3,4)
    screen.fill(BACK_GROUND)

    game_view.draw(screen,game_model)
    pygame.display.flip()