import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS(some icon thing)
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Example usage:
# my_icon = resource_path("my_icon.ico")(also some icon thing)

import turtle   #basic stuff
s = turtle.Screen()
s.title("Digi-Etch-A-Sketch by Saikathir v1.5.5")
player = turtle.Turtle()
player.write("Welcome to Digi-Etch-A-Sketch v 1.5.5. 1-4 for pen sizes, QWERTY for colors, and press Z and X for penup and pendown. Press Backspace to clear this message!")
def move_forward():   #defining functions
    player.forward(50)


def move_left():
     player.left(45)


def move_backward():
    player.backward(50)


def move_right():
    player.right(45)


def clear():
    player.clear()


def size1():
    player.pensize(1)


def size2():
    player.pensize(2)


def size3():
    player.pensize(3)


def size4():
    player.pensize(4)

def red():
    player.color("red")


def yellow():
    player.color("yellow")


def green():
    player.color("green")


def blue():
    player.color("blue")


def black():
    player.color("black")


def white():
    player.color("white")


def penup():
    player.penup()


def pendown():
    player.pendown()



s.listen()
s.onkey(move_forward, "Up")     #behold, the wall of assigning keypresses to random functions!
s.onkey(move_backward, "Down")
s.onkey(move_left, "Left")
s.onkey(move_right, "Right")
s.onkey(clear, "BackSpace")
s.onkey(size1, "1")
s.onkey(size2, "2")
s.onkey(size3, "3")
s.onkey(size4, "4")
s.onkey(red, "q")
s.onkey(yellow, "w")
s.onkey(green, "e")
s.onkey(blue, "r")
s.onkey(black, "t")
s.onkey(white, "y")
s.onkey(penup,"z")
s.onkey(pendown,"x")
turtle.done()
