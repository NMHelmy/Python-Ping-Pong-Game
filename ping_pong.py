# imported turtle module
import turtle

player1 = input("Player 1: ")
player2 = input("Player 2: ")

# window or screen that will show the game
wind = turtle.Screen()  # initialize screen
wind.title("Ping Pong")  # sets the title of the window
wind.bgcolor("black")  # sets the background color of the window
wind.setup(width=800, height=600)  # sets the width and height of the window
wind.tracer(0)  # stops the window from updating automatically

# racket 1
racket1 = turtle.Turtle()  # initializes tutle object(shape)
racket1.speed(0)  # sets the speed of the animation
# not the moving the speed, but the speed of drawing the pixels on the screen, the fastest speed = 0
racket1.shape("square")  # sets the shape of the object
racket1.color("red")  # sets the color of the shape
# it automatically sets the size of the shape to 20x20 pixels
racket1.shapesize(stretch_wid=5, stretch_len=1)  # stretching the shape from the 20 pixels
racket1.penup()  # pulling pen up, stops the object from drawing lines when moving
racket1.goto(-350, 0)  # sets the position of the object

# racket 2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("blue")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.penup()
racket2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # every time the ball moves on screen it will move ## pixels
ball.dy = 0.2  # the larger the number the faster the object

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("yellow")
score.penup()
score.hideturtle()  # to hide the object we just want to see the text
score.goto(0, 260)
score.write(player1 + ": 0 " + player2 + ": 0", align="center", font=("courier", 14, "normal"))

# text to identify how many points are needed to win
text = turtle.Turtle()
text.color("white")
text.penup()
text.hideturtle()
text.goto(386, -286)
text.write("*score 15 points*", align="right", font=("courier", 14, "italic"))

def racket1_up():
    y = racket1.ycor()  # function in turtle module that gets the y coordinate of the object
    y += 20  # as you go up the object will move 20 pixels
    racket1.sety(y)  # updates the y coordinates when it moves


def racket1_down():
    y = racket1.ycor()
    y -= 20
    racket1.sety(y)


def racket2_up():
    y = racket2.ycor()
    y += 20
    racket2.sety(y)


def racket2_down():
    y = racket2.ycor()
    y -= 20
    racket2.sety(y)


# keyboard bindings
wind.listen()  # tells the window to expect keyboard input
wind.onkeypress(racket1_up, "w")  # when the w key (has to be lower case) is pressed calls function
wind.onkeypress(racket1_down, "s")
wind.onkeypress(racket2_up, "Up")  # arrow upward
wind.onkeypress(racket2_down, "Down")  # arrow downward

# main game loop
while True: # loop stops manually or until some external event like closing the window, interrupts the execution
    wind.update()
    # updates the screen everytime the loop runs

    # move the ball
    ball.setx(ball.xcor() + ball.dx)  # ball starts at 0 and everytime the loop runs --> +0.2 on x axis
    ball.sety(ball.ycor() + ball.dy)  # ball starts at 0 and everytime the loop runs --> +0.2 on y axis
    # the new position of the ball is the x/y coordinates of the ball plus the 0.2
    # first coordinate is 0 then add 0.2 and loop

    # border check , top border +300px, bottom border -300px, ball 20px
    if ball.ycor() > 290:  # if the ball hits the top of the screen (300 as the ball is 20 pixels - 10 top & 10 bottom)
        ball.sety(290)  # update the y coordinates to 290
        ball.dy *= -1  # and reverse direction as you multiply by -1

    if ball.ycor() < -290:  # if ball hits the bottom of the screen
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:  # if ball hits the right border, width of the positive part is 400
        ball.goto(0, 0)  # returning ball to the center, lose by touching the sides
        ball.dx *= -1
        score1 += 1
        score.clear()  # deletes the previous text to print the new one
        score.write(player1 + ": {} ".format(score1), align="right", font=("courier", 14, "normal"))
        score.write(player2 + ": {} ".format(score2), align="left", font=("courier", 14, "normal"))
        # {}.format() automatically updates the score

    if ball.xcor() < -390:  # if ball hits the left border
        ball.goto(0, 0)  # lose by touching the sides
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(player1 + ": {} ".format(score1), align="right", font=("courier", 14, "normal"))
        score.write(player2 + ": {} ".format(score2), align="left", font=("courier", 14, "normal"))

    # racket hitting the ball
    if (340 < ball.xcor() < 350) and (racket2.ycor() - 40 < ball.ycor() < racket2.ycor() + 40):
        # racket is at 350 (x coordinates) - 10 of the ball = 340
        # 340 as the ball is 20px, racket width is 20px and length is 100px
        # so 50 above x-axis and 50 below x-axis, width 400
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (racket1.ycor() - 40 < ball.ycor() < racket1.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1

    if score1 == 15:
        score.sety(0)
        score.color('red')
        style = ('Courier', 80, 'italic')
        score.write(" WINNER:", align="center", font=style)
        score.sety(-80)
        score.write(player1.upper(), align="center", font=style)
        break
    elif score2 == 15:
        score.sety(0)
        score.color('blue')
        style = ('Courier', 80, 'italic')
        score.write(" WINNER:", align="center", font=style)
        score.sety(-80)
        score.write(player2.upper(), align="center", font=style)
        break
    else:
        continue

turtle.exitonclick()
