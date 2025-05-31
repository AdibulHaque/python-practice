#This is a short and dealt with the looping problem. 
# Here I tried just to change the looping course to left and make sure it not loops in the same course.
# Maze - Version 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        if front_is_clear() and right_is_clear():
            while right_is_clear():
                turn_right()
                move()
                turn_left()
                break
            
    elif front_is_clear():
        move()
    else:
        turn_left()