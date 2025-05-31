# Here i just make sure that there is wall in front of the robot, so it can start moving. and not fall into a loop
# Maze - Version 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Making sure that it have a wall in front
while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
        
        
        
