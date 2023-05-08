import turtle
turtle.setup(800,600)
window=turtle.Screen()
window.title("Star")
t1=turtle.Turtle()
t1.showturtle()
t1.fillcolor("red")
print("Turtle Window")
print("*************")
for i in range(5):
 t1.forward(100)
 t1.right(144)