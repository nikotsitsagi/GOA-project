from turtle import*
speed(200)




#ground
width(5)
penup()
goto(0 , -100)
pendown()
color("green")
begin_fill()
right(180)
forward(900)
left(90)
forward(1800)
left(90)
forward(1800)
left(90)
forward(1800)
left(90)
forward(900)
end_fill()





#first floor (first side)
color("gray")
begin_fill()
penup()
goto(450 , -100)
pendown()
color("gray")
right(90)
forward(300)
left(90)
forward(60)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
end_fill ()

#second side
penup()
color ("gray")
begin_fill()
goto(0 , -100)
goto(-450 , -100)
pendown()
left(180)
forward(300)
right(90)
forward(60)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(60)
end_fill()



#the roof
penup()
goto(210 , 170)
pendown()
color("gray")
begin_fill()
left (180)
forward(420)
right (90)
forward (200)
right(90)
forward(420)
right(90)
forward(200)
end_fill()


#window 1
color("cyan")
begin_fill()
penup()
goto(170, 240)
pendown()
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()
right(90)
forward(30)
right(90)
color("black")
forward(60)
color("cyan")
left(90)
forward(30)
left(90)
forward(30)
left(90)
color("black")
forward(60)

#window 2
color("cyan")
begin_fill()
penup()
goto(-100 , 240)
pendown()
left(90)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()
right(90)
forward(30)
right(90)
color("black")
forward(60)
color("cyan")
left(90)
forward(30)
left(90)
forward(30)
left(90)
color("black")
forward(60)


end_fill()

#door
color("brown")
begin_fill()
penup()
goto(70 , -100)
pendown()
left(90)
forward(200)
left(90)
forward(140)
left(90)
forward(200)
left(90)
forward(140)
end_fill()
left(180)
forward(70)
color("black")
right(90)
forward(200)
right(180)
forward(100)
right(90)
color("dark gray")
begin_fill()
penup()
goto(-55 , 0)
pendown()
circle(10)
end_fill()

color("black")
penup()
goto(450 , 200)
begin_fill()
pendown()
right(90)
forward(100)
right(90)
forward(90)
right(90)
forward(50)
right(90)
forward(90)
end_fill()












exitonclick()
