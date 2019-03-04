#main folder, where all the game is
from turtle import *
import turtle
import time 
import random
import math
from functions import *
from tkinter import *
from characters import *

global score_count
#higher tracer = faster characters spawning from the left
turtle.tracer(125,1)

#main character is Abed
turtle.register_shape("abed.gif")
abed = Player (20)
abed.shape("circle")
abed.shapesize(1)
abed.penup()
	

#life and score counters
Life = 3

#life hearts
turtle.register_shape("hearts0.gif")
turtle.register_shape("hearts1.gif")
turtle.register_shape("hearts2.gif")
turtle.register_shape("hearts3.gif")
hearts=turtle.Turtle()
hearts.penup()
hearts.shape("hearts3.gif")
hearts.goto(-700, 450)

#score counter
score_count = 0
score=turtle.Turtle()
score.penup()
score.hideturtle()
score.goto(200,450)
score.write(str("SCORE: " + str(score_count)),move=True,align = "center",font=("CHARLESWORTH",25,"bold"))


#game over 
turtle.register_shape("gameover.gif")
gameover=turtle.Turtle()
gameover.shape("gameover.gif")
gameover.hideturtle()

#you win
turtle.register_shape("okhand.gif")
win=turtle.Turtle()
win.shape("okhand.gif")
win.hideturtle()

#controls for the player
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP

#creating the tables to place food on
foods=[burger,pizza,sushi]
FOODCOLLISION= False
table=Food(200,280,40)
table2=Food(200,70,40)
table3=Food(200,-150,40)
table4=Food(200,-360,40)
tables = [table,table2,table3,table4]


#controls
def up():
	global direction
	direction=UP 
	abed.goto(abed.xcor(), abed.ycor() + 55)#change this value to change the speed at Abed moves
def down():
    global direction
    direction = DOWN
    abed.goto(abed.xcor(), abed.ycor() - 55)#change this value to change the speed at Abed moves

def left():
    global direction
    direction = LEFT
    abed.goto(abed.xcor() - 55, abed.ycor())#change this value to change the speed at Abed moves

def right():
    global direction
    direction = RIGHT
    abed.goto(abed.xcor() + 55, abed.ycor())#change this value to change the speed at Abed moves

turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

#making the collide function, essential for the rest of the game
def collide(ball_a,ball_b):
	x1=ball_a.xcor()
	x2=ball_b.xcor()
	y1=ball_a.ycor()
	y2=ball_b.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D >= ball_a.r + ball_b.r:
		return False
	if D < ball_a.r + ball_b.r:
		return True

#checking if Abed has collided with the food on the right 
def check_food_collision():
	for f in foods:
		if collide(abed,f) == True:
			#showing the food whenever Abed touches it
			f.showturtle()
			#making the food follow abed whenever he picks them up
			f.goto(abed.xcor(),abed.ycor())
					
	return True

#checking if the food has collided with the tables and making sure they are alligned for desire_food_player collsion
def slide_food():
	global number
	for f in foods:
		for t in tables:
			if collide(f,t) == True:
				#making the food go to the begining of the table
				f.goto(t.xcor(),t.ycor())
				#making the food move a bit to the left whenever it touches the table
				f.bk(50)

	return True

#biggest function, checking the collision between customer requests, the customers, and the food
def check_food_desire_player_collision():
	global Life,score_count,score
	for a in foods:
		for b in desires:
			for c in players:
				if collide(a,c) == True and collide(a,b):
					#checking if the food given to the customer is the correct one
					if a.shape() == b.shape():
						#hiding the food giving the impression a customer is "satisfied"
						a.hideturtle()
						#increases score
						
						score_count += 25
						score.clear()
						score.goto(200,450)
						score.write(str("SCORE: " + str(score_count)),move=True,align = "center",font=("CHARLESWORTH",25,"bold"))
						#random value to decide new picture for customers
						e = random.randint(0,4)
						c.shape(shapes[e])
						#random value to decide the new position the customer will go to
						p = random.randint(0,3)
						c.goto(starting_positions[p])
						#random value to decide new customer request
						g = random.randint(0,2)
						b.shape(food_choices[g])
						#making the request of the customer follow the customer
						b.goto(c.xcor()+90, c.ycor()-50)
						#after the food collides, it goes back to its starting positions on the right
						if a == pizza:
							a.goto(570,130)
						elif a == sushi:
							a.goto(650,-50)
						else:
							a.goto(450,290)

					else:
						#same as top except we subtract a point from life
						Life -= 1
						a.hideturtle()
						e = random.randint(0,4)
						c.shape(shapes[e])
						p = random.randint(0,3)
						c.goto(starting_positions[p])
						g = random.randint(0,2)
						b.shape(food_choices[g])
						b.goto(c.xcor()+90, c.ycor()-50)
						if a == pizza:
							a.goto(570,130)
						elif a == sushi:
							a.goto(650,-50)
						elif a == burger:
							a.goto(450,290)
						if Life == 3:
							hearts.shape("hearts3.gif")
						elif Life == 2:
							hearts.shape("hearts2.gif")
						elif Life == 1:
							hearts.shape("hearts1.gif")

#this funcion checks if the customers have reached too far on the table and they sacrifice a Life
def check_if_player_reached_table():
	global Life
	for a in desires:
		for b in players:
			if a.xcor() > 200 and b.xcor() > 150:
				Life -= 1
				e = random.randint(0,4)
				b.shape(shapes[e])
				p = random.randint(0,3)
				b.goto(starting_positions[p])
				g = random.randint(0,2)
				a.shape(food_choices[g])
				a.goto(b.xcor()+90, b.ycor()-50)
				if Life == 3:
					hearts.shape("hearts3.gif")
				elif Life == 2:
					hearts.shape("hearts2.gif")
				elif Life == 1:
					hearts.shape("hearts1.gif")

#listen so the keys can control Abed		
turtle.listen()

frame = 0

#main loop to make game move
while Life > 0:	
	check_food_collision()
	frame+=1
	#change the value in frame/x to control how often players spawn
	if frame/2000 == 1:
		frame = 0
		spawn_player()
	move_players()
	move_desires()
	check_food_desire_player_collision()
	check_if_player_reached_table()
	slide_food()
	turtle.update()
	if score_count//25 == 1000000:
		abed.hideturtle()
		hearts.hideturtle()
		for a in players:
			a.hideturtle()
		for d in desires:
			d.hideturtle()
		turtle.bgpic("okhand.gif")

#this section plays whenever you lose
while Life == 0:
	hearts.shape("hearts0.gif")
	gameover.showturtle()
	abed.hideturtle()
	for a in players:
		a.hideturtle()
	for d in desires:
		d.hideturtle()


turtle.mainloop()