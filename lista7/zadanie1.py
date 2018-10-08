from turtle import *
 
def snowflake(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)
    right(120)
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)
 
if __name__ == "__main__":
    # defining the speed of the turtle
    speed(0)                   
    length = 500.0  
 
    # Pull the pen up – no drawing when moving.
    # Move the turtle backward by distance, opposite
    # to the direction the turtle is headed.
    # Do not change the turtle’s heading.           
    penup()                     
 
    backward(length/2.0)
 
    # Pull the pen down – drawing when moving.        
    pendown()           
    for i in range(3):    
        snowflake(length, 3)
        tracer(0,0)
        right(120)
    update()
     # To control the closing windows of the turtle
    mainloop()    