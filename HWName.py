Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle forward(100)
SyntaxError: invalid syntax
>>> turtle.forward(100)
>>> turtle.rigth(135)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    turtle.rigth(135)
AttributeError: module 'turtle' has no attribute 'rigth'
>>> turtle.right(135)
>>> turtle.forward(120)
>>> turtle.penup()
>>> turtle.goto(120,0)
>>> turtle.forward(120)
>>> turtle.undo()
>>> turtle.pendown()
>>> turtle.left(135)
>>> turtle.left(90)
>>> turtle.left(90)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.penup()
>>> turtle.goto(130,0)
>>> turtle.undo()
>>> turtle.goto(0, -120)
>>> turtle.left(90)
>>> turtle.pendown()
>>> turtle.forward(100)
>>> turtle.forward(20)
>>> turtle.forward(120)
>>> turtle.undo()
>>> turtle.left(90)
>>> turtle.undo()
>>> turtle.right(90)
>>> turtle.forward(120)
>>> turtle.right(90)
>>> turtle.forward(120)
>>> turtle.right(90)
>>> turtle.forward(120)
>>> turtle.pendown()
>>> turtle.penup()
>>> turtle.goto(0, 150)
>>> turtle.undo()
>>> turtle.goto(150,0)
>>> turtle.right(90)
>>> turtle.pendown()
>>> turtle.forward(120)
>>> turtle.right(90)
>>> turtle.forward(120)
>>> turtle.right(90)
>>> turtle.forward(120)
>>> turtle.right(90)
>>> turtle.forward(120)
>>> turtle.right(90)
>>> turtle.penup()
>>> turtle.goto(320,0)
>>> turtle.pendown()
>>> turtle.forward(120)
>>> turtle.right(90)
>>> turtle.forward(60)
>>> turtle.right(90)
>>> turtle.forward(120)
>>> turtle.right(90)
>>> turtle.right(90)
>>> turtle.right(90)
>>> turtle.forward(60)
>>> turtle.right(90)
>>> 
>>> turtle.right(90)
>>> turtle.right(90)
>>> turtle.forward(120)
>>> turtle.penup()
>>> turtle.goto (440, 30)
>>> turtle.undo()
>>> turtle.goto(440,-30)
>>> turtle.pendown()
>>> turtle.forward(30)
>>> turtle.pendown()
>>> turtle.goto(440,-60)
>>> turtle.undo()
>>> turtle.penup()
>>> turtle.goto(440,-60)
>>> turtle.pendown()
>>> turtle.forward(30)
>>> turtle.penup()
>>> turtle.goto(440,0)
>>> turtle.goto(470,0)
>>> turtle.right(90)
>>> turtle.forward(120)
>>> turtle.undo()
>>> turtle.pendown()
>>> turtle.forward(120)
>>> turtle.penup()
>>> turtle.Pen(400,0)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    turtle.Pen(400,0)
  File "D:\Python\lib\turtle.py", line 3814, in __init__
    RawTurtle.__init__(self, Turtle._screen,
  File "D:\Python\lib\turtle.py", line 2546, in __init__
    self.turtle = _TurtleImage(screen, shape)
  File "D:\Python\lib\turtle.py", line 2489, in __init__
    self._setshape(shapeIndex)
  File "D:\Python\lib\turtle.py", line 2503, in _setshape
    self._type = screen._shapes[shapeIndex]._type
KeyError: 400
>>> turtle.goto(400,0)
>>> turtle.goto(400,-300)
>>> turtle.goto(400,-100)
>>> turtle.goto(400,-120)
>>> turtle.goto(400,-140)
>>> turtle.goto(400,-160)
>>> turtle.goto(400,-180)
>>> turtle.goto(400,-190)
>>> turtle.pendown()
>>> turtle.circle(30)
>>> turtle.undo()
>>> turtle.circle(60)
>>> 