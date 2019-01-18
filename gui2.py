import pygame
import time
import random

pygame.init()
width_d = 800
height_d = 600

# Colour defn
black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
back_colour = (210,210,210)

car_width = 80 # h = 85
car_height = 85

gameDisplay = pygame.display.set_mode((width_d,height_d))  # window size

pygame.display.set_caption('A bit Racey') # window title

carImg = pygame.image.load('car2.png')
def things(thingx, thingy, thingh, thingw, colour):
	pygame.draw.rect(gameDisplay, colour, [thingx, thingy, thingh, thingw])
def car(x,y):
	gameDisplay.blit(carImg, (x,y)) # put car on screen
def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()
def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged : "+ str(count), True, black)
	gameDisplay.blit(text, (0,0))
def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((width_d//2), (height_d//2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(2)
	game_loop()

def crash():
	message_display('You crashed')

def game_loop():

	x = (width_d * 0.45)
	y = (height_d * 0.8)
	x_change = 0


	thing_starty = -600
	thing_speed = 3
	thing_width = 100
	thing_height = 100
	thing_startx = random.randrange(10, width_d - thing_width - 10)
	
	dodged = 0
	# Define game clock ... like fps
	clock = pygame.time.Clock()

	# We need a game loop .. to update game

	gameExit = False # We get out of loop if we crash or sth

	while not gameExit:
		for event in pygame.event.get():
			# Gets a list of all events that have happened
			# in every frame
			if event.type == pygame.QUIT:
				# If cross is clicked
				# We can ask "are you sure" etc
				pygame.quit()   # stops running pygame
				# Run any other quitting function
				quit()


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					x_change = 0

		x+= x_change
		gameDisplay.fill(back_colour)

		# things(thingx, thingy, thingh, thingw, colour):
		things(thing_startx, thing_starty, thing_width, thing_height, black)
		thing_starty += thing_speed
		car(x,y)
		things_dodged(dodged)

		if x > width_d - car_width or x<0:
			crash()
		if thing_starty > height_d:
			thing_starty = -thing_height
			thing_startx = random.randrange(10, width_d - thing_width - 10)
			dodged+=1
			# thing_speed +=1
			if width_d - thing_width - 10>11 and thing_width<width_d//2:
				thing_width += int(dodged*1.2)

		if y<thing_starty+thing_height and y+car_height>thing_starty:
			if x+car_width> thing_startx and x< thing_startx+thing_width :
				crash()




		pygame.display.update()  # updates the display
		clock.tick(120) # This number is FPS

game_loop()

pygame.quit()   # stops running pygame

# Run any other quitting function
quit()



