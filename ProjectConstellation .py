#Danica Cordova
#May 31, 2019
#Version16

import turtle

turtle.hideturtle() #This hides the turtle pointer visibility.

#I wanted the graphic to draw in a specific flow,
#working from left to right and from top to bottom.

#I started with the left/uppermost star.

turtle.penup() #This hides the graphic movement from the default point (0,0) to my starting point (-110,160).
turtle.goto(-100,160) #I used this function to easily move from one plot to the next.
turtle.pendown()
turtle.dot() #indicator for the star plots
turtle.write("Betelgeuse") #labeling the star

turtle.goto(-30,-10)
turtle.dot()
turtle.write("Alnitak")

turtle.goto(-80,-140)
turtle.dot()
turtle.write("Saiph")

turtle.penup() #This function is meant to return to the star, Alnitak,
turtle.goto(-30,-10)#so that the graphic doesn't draw from Saiph to Alnilam.
turtle.pendown()

turtle.goto(0,0)
turtle.dot()
turtle.write("Alnilam")

turtle.goto(30,10)
turtle.dot()
turtle.write("Mintaka")

turtle.goto(80,140)
turtle.dot()
turtle.write("Melissa")

turtle.penup() #Similar to the previous function, this is meant to first return to Mintaka
turtle.goto(30,10) #so the graphic doesn't draw from Melissa to Rigel.
turtle.pendown()

turtle.goto(80,-120)
turtle.dot()
turtle.write("Rigel")
