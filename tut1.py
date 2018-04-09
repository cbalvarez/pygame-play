import sys, pygame

pygame.init()

size = width, height = 1020, 720
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball3.png")
ballrect = ball.get_rect()
ballact = "ball3"

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
	if event.type == pygame.KEYDOWN:
		if ( event.key == pygame.K_UP):
			speed[0] = speed[0] * 1.1	
			speed[1] = speed[1] * 1.1	
		if ( event.key == pygame.K_DOWN):
			speed[0] = speed[0] / 1.1	
			speed[1] = speed[1] / 1.1	
		if ( event.key == pygame.K_RIGHT):
			speed[0] = speed[0] * 1.1
		if ( event.key == pygame.K_TAB):
    			screen.fill(black)
			if (ballact == "ball3"):
				ball = pygame.image.load("ball2.png")
				ballact= "ball2"
			elif (ballact == "ball2"):
				ball = pygame.image.load("ball3.png")
				ballact = "ball3"
			ballrect = ball.get_rect()
    			screen.blit(ball, ballrect)
    			pygame.display.flip()
	

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
