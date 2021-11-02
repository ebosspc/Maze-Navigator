#Import Turtle library for functions that will be used later
import turtle as trtl

#Maze and turtle configuration values
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#Robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#Initialize display Screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#Initialize starting robot conditions
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#Display maze
wn.bgpic("maze2.png") # other file names should be maze2.png, maze3.png

#Firt Robot Movement navigation

#Counting Variables
a = 0 
b = 0
c = 0
d = 0

#While loop to make the robot go up 3 spaces
while (a < 3):
  move()
  a = a+1

#While loop to make the robot turn to the right
while(b < 3):
  turn_left()
  b = b + 1

#While loop to make the robot move to the right 2 spaces
while(c < 2):
  move()
  c = c + 1

#Reset back to original points and conditions
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#Second Robot movement Navigation

#Counting Variables
a = 0 
b = 0
c = 0
d = 0

#While loop to face right
while (a < 3):
  turn_left()
  a = a + 1

#Nested while loop to move right three spaces, then turn left
while (b < 2):

  while (c < 3):
    move()
    c = c + 1
  c = 0

  turn_left()
  b = b + 1
move() #Move left into grey square

#Screen Display
wn.mainloop()
