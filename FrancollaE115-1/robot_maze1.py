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
wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

#Robot Movement navigation

#Counting Variables
a = 0 
turn_right = 0
b = 0
 
#While Loop to move up 4 spaces
while (a < 4):
  move()
  a = a + 1

#While loop to turn right
while(turn_right < 3):
  turn_left()
  turn_right = turn_right + 1

#While Loop to the right 4 spaces
while (b < 4):
  move()
  b = b + 1

#Screen Display
wn.mainloop()
