def turn_circle():
    while at_goal() != True:
        if front_is_clear() == True and wall_in_front() == False:
            move()
        elif front_is_clear() == True:
            circle1()
        elif wall_in_front() == True:
            circle2()
        else:
            move()
            

def circle2():
    turn_left()
    move()
    move_right()
    move()
    move_right()
    move()
    turn_left()
def circle1():  
    move()
    turn_left()
    move()
    move_right()    
    move()    
    move_right()    
    move()
    turn_left()
def move_right():
    turn_left()
    turn_left()
    turn_left()
turn_circle()
