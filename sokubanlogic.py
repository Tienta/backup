#Vetors : x,y : Dictionary or x,y it self
Map
Player

#List of vetors : List of numbers of dictionary
Boxes
Walls
Points



4. Map
Ownership: Height and width --> x,y or [x,y] or {"x":0,"y":0}
Contain Player, Boxes, Points, Walls
--> def print map --> def check position == x,y of map to print?

--> def Check in map or not : 0< the next_position() <= map width and height
--> def Check collide : next_position() == walls_position
--> def move(obj, dx,dy)
--> def next_position
--> def input_direction


3 --> 2 --> 1 --> 4

3. Walls/points
Owership ; direction dictionary
action: Stand only

2.Boxes:
- Move:
    - conditionar:
        Depend on player next_move
        Move 1 step only
        Can not go out of map
        Can not move through the walls


1. Player:
Player ownership : x, y

Action:
- Move:
    - conditionar:
        Move multiple direction
        Move 1 step only
        Can not go out of the map
        Can not move through the walls

- Push box : logic : if the next_move_player == the position of the box then position_box = next_position

