#last file making alot of photos
from turtle import *
import turtle
import random
import time

#assigning the background photo
sc = turtle.Screen()
sc.setup(1700,1080)
turtle.bgpic("tapperbg.gif")


#making the photos the random customers will be
turtle.register_shape("joyce.gif")
turtle.register_shape("km.gif")
turtle.register_shape("mahd.gif")
turtle.register_shape("sadeen.gif")
turtle.register_shape("shawerma.gif")

#very important lists for the rest of the game
food_choices = ["burger1.gif", "pizzaf.gif", "sushi.gif"]
desires = []
players = []
shapes = ["joyce.gif", "km.gif", "mahd.gif", "sadeen.gif", "shawerma.gif"]


#the 4 starting positions the customers can spawn in the left
starting_positions = []
start_pos1 = (-800,335)
starting_positions.append(start_pos1)
start_pos2 = (-800,135)
starting_positions.append(start_pos2)
start_pos3 = (-800,-75)
starting_positions.append(start_pos3)
start_pos4 = (-800,-285)
starting_positions.append(start_pos4)


#making the class for the random characters that spawn in the left
class Players(Turtle):
	def __init__(self,dx,dy,r):
		Turtle.__init__(self)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.penup()
		self.shape("circle")
		self.shapesize(1)
		self.speed(0)
	
	def move(self):
		self.forward(.1)


#making the class for the customer's requests
class Desires(Turtle):
	def __init__(self,r):
		Turtle.__init__(self)
		self.penup()
		self.shape("circle")
		self.r = r

	def move(self):
		self.forward(.1)



				
#making the function that spawns the players in the left, giving them random starting positions and random photos
def spawn_player():  
	if len(players) < 5:
		player1 = Players(100,5,75)
		players.append(player1)
		desire1 = Desires(40)
		desires.append(desire1)
		p = random.randint(0,3)
		a = random.randint(0,4)
		g = random.randint(0,2)
		player1.shape(shapes[a])
		desire1.shape(food_choices[g])
		player1.goto(starting_positions[p])
		desire1.goto(player1.xcor()+90, player1.ycor()-50)


#move functions
def move_players():
	for player in players:
		player.move()
def move_desires():
	for desire in desires:
		desire.move()

#making sure the player list keeps getting updated
def getplayers():
	return players