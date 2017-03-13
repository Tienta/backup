from models.gamemodel import GameModel

#Unit Test

#Test 1
game_models = GameModel(2,3)
game_models.print()

#Test 2 : Test move
game_models.x = 2
game_models.y = 3
game_models.move(1,-1)
assert (game_models.x == 3 and game_models.y == 2)

#Test 3 : Test next_move : - change value on def next_move and - not change value on def move
game_models.x = 5
game_models.y = 4
[next_x, next_y]=game_models.calc_next_pos(1,-2)
assert (next_x == 6) and (next_y == 2)
assert game_models.x == 5 and game_models.y == 4



