from turtle import *
hideturtle()
fillcolor('red')
speed(2)
begin_fill()
for i in [200, 100] * 2:
	fd(i)
	circle(30, 90)
end_fill()
penup()
goto(80, 50)
pendown()
fillcolor('white')
pencolor('white')
begin_fill()
left(90)
fd(60)
right(120)
fd(60)
right(120)
end_fill()

penup()
goto(-30, -90)
pendown()
pencolor('black')
write("YouTube" ,font=("Roboto",50))

done()