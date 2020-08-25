import turtle
import random
import time
scoreL = 0
scoreR = 0


win = turtle.Screen()
win.title("PONG")
win.bgcolor("black")
win.setup(width=1200,height=800)
win.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Gracz A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

paddleL = turtle.Turtle()
paddleL.speed(0)
paddleL.shape("square")
paddleL.color("white")
paddleL.shapesize(stretch_wid=5,stretch_len=1)
paddleL.penup()
paddleL.goto(-550, 0)

paddleR = turtle.Turtle()
paddleR.speed(0)
paddleR.shape("square")
paddleR.color("white")
paddleR.shapesize(stretch_wid=5,stretch_len=1)
paddleR.penup()
paddleR.goto(550, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.xd , ball.yd = 1,1 #1 or -1

win.listen()
win.onkeypress(lambda paddle = paddleL: paddleMove(paddle,20), "w")
win.onkeypress(lambda paddle = paddleL: paddleMove(paddle,-20), "s")
win.onkeypress(lambda paddle = paddleR: paddleMove(paddle,20), "Up")
win.onkeypress(lambda paddle = paddleR: paddleMove(paddle,-20), "Down")

def paddleMove(panddle,y):

    yCor = panddle.ycor()
    y =yCor+y
    if y >-380 and y<380:
        panddle.sety(y)

def ballSpeed():
    return [random.randint(1,4) , random.randint(1,4)] #[x,y]
def resetBall():
        pen.clear()
        pen.write("Gracz A: {}  Gracz B: {}".format(scoreL, scoreR), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.xd *= -1
        ball.yd *= -1
xs,ys = ballSpeed()
while(True):
    
    win.update()
    ball.sety(ball.ycor()+ball.yd*ys)
    ball.setx(ball.xcor()+ball.xd*xs)
    
    # Top and bottom
    if ball.ycor() > 390:
        ball.sety(390)
        ball.yd *= -1
    
    elif ball.ycor() < -390:
        ball.sety(-390)
        ball.yd *= -1

    # Left and right
    if ball.xcor() > 550:
        scoreL += 1
        resetBall()
        xs,ys = ballSpeed()

    elif ball.xcor() < -550:
        scoreR += 1
        resetBall()
        xs,ys = ballSpeed()

    # Paddle and ball collisions
    if ball.xcor() < -540 and ball.ycor() < paddleL.ycor() + 50 and ball.ycor() > paddleL.ycor() - 50:
        ball.xd *= -1 
        xs,ys = ballSpeed()
    
    elif ball.xcor() > 540 and ball.ycor() < paddleR.ycor() + 50 and ball.ycor() > paddleR.ycor() - 50:
        ball.xd *= -1
        xs,ys = ballSpeed()
    time.sleep(1 / 90)
