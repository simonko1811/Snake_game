 #snake-like game
import turtle
import time
import random
import gc

delay = 0.1

#score init
score = 0
high_score = 0

#set up window
wn = turtle.Screen()
wn. title("My Snake game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off screen updates

#creating snake head
head = turtle.Turtle()
head.speed(0) #animation speed - 0 = MAX
head.shape("square")
head.color("black")
head.penup() #do not draw
head.goto(0, 0) #start at center of window
head.direction = "stop" #direction to go from start

#snake food
food = turtle.Turtle()
food.speed(0) #animation speed - 0 = MAX
food.shape("circle")
food.color("red")
food.penup() #do not draw
food.goto(0, 100) #start at center of window

segments = []

#pen
pen = turtle.Turtle()
pen.speed()
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"


#function to move head of snake
def move():
    if head.direction == "up":
        y = head.ycor() #y coordinate
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor() #y coordinate
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor() #x coordinate
        head.setx(x + 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20) #can be done this way too

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w") #call go_up on w key pressed, can be up arrow - "Up"
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

#main game loop
while True:
    wn.update()

    #chech for border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1) #sleep 1 sec
        head.goto(0, 0)
        head.direction = "stop"

        #hide segments after reset
        for segment in segments:
            segment.hideturtle()
            segment.clear()

        segments.clear()

        #reset score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    #checking for getting food
    if head.distance(food) < 20: #20 is distance between center of head and center of food
        #move food to random spot
        x = random.randint(-14, 14)*20 #to be precise, and get odd number or somewhere bwtween 0 and 20
        y = random.randrange(-280, 280, 20) #doing the same as for x, but with different function (from, to, step)
        food.goto(x, y)

        #add a segment to snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #increase score
        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #move end segments first in reverse
    for index in range(len(segments)-1, 0, -1): #(from where, to where, by how much)
       x = segments[index-1].xcor()
       y = segments[index-1].ycor()
       segments[index].goto(x, y)

    #move segment 0 to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #check for body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"
            #hide segments after reset
            for segment in segments:
                segment.hideturtle()
                segment.clear()
            segments.clear()

            #reset score
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)

wn.mainloop()