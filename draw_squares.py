import turtle

def draw_squares():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(0)
    
    for count2 in range(4):        
        brad.forward(100)
        brad.right(90)
  
    window.exitonclick()
    
draw_squares()
