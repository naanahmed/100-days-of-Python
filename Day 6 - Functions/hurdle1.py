def turn_right():
    turn_left()
    turn_left()
    turn_left()

def complete():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for _ in range(6):
    complete()