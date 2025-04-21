#This is a comment
#1 Install my library
import pgzrun
from random import randint

#2 Background
WIDTH=400
HEIGHT=400
Score=0

#Create a variable for our actor


#Drawing my actor on the screen
def draw():
	#change the background color 
	screen.fill("white")
	#Draw your actor
	#change the score text color 
	screen.draw.text("Score: "+ str(Score),color="black", topleft=(10,10))


#My function to change the position of my actor
# on the screen
def Move():
	#Change your X and Y
	My_Player.x=randint(10,WIDTH)
	My_Player.y=randint(10,HEIGHT)

#this means get the position of mouse when I click
def on_mouse_down(pos):
	global Score
	#Check if click and actor are on the same place
	

pgzrun.go()#This is to run my program