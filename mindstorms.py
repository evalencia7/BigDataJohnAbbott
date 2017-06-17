import turtle

def draw_circle_of_squares(angle):
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(0)

    turn_angle = angle
    
    for count1 in range (360/turn_angle) :
        for count2 in range(4) :
            brad.forward(100)
            brad.right(90)
        brad.right(angle)

    window.exitonclick()
    
draw_circle_of_squares(10)
