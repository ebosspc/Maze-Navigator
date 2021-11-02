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
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#Robot Movement Navigation

#Counting Variables
a = 0 
b = 0
c = 0
d = 0

#While and nested while loops to move up and to the right diagonally 
while (a < 4):

  #Nested while loop to turn right
  while (b < 3):
    turn_left()
    b = b + 1

  #While loop to move foward and turn left
  while (c < 1):
    move()
    turn_left()
    move()
    c = c + 1

  #Reset b and c to 0 so the nested whiel loop can repeat over multiple iterations
  b = 0
  c = 0
  
  a = a + 1

#Screen Display
wn.mainloop()
