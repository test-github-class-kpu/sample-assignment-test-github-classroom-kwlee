import turtle

def drawTree(branch,t):
    if branch > 5:
        t.forward(branch)
        t.right(20)
        drawTree(branch-15,t)
        t.left(40)
        drawTree(branch-15,t)
        t.right(20)
        t.backward(branch)

def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    drawTree(100, t)
    window.exitonclick()

main()
