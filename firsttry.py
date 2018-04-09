import sys, pygame


class DriftStatus:
	def __init__(self,cycles):
		self.cycles = cycles
		self.orig_speed = None

	def isEnd(self):
		return self.cycles_left == 0

	def wasteCycle(self):
		self.cycles_left = self.cycles_left -1

	def changeVectorOrigSpeed(self):
		if (self.orig_speed is not None):
			self.orig_speed = -1 * self.orig_speed 

	def isActive(self):
		return self.orig_speed is not None

	def inactivate(self):
		self.orig_speed = None

	def start(self, orig_speed):
		self.orig_speed = orig_speed
		self.cycles_left = self.cycles

	





pygame.init()

size = width, height = 1020, 720
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball3.png")
ballrect = ball.get_rect()
ballact = "ball3"


rightDrift = DriftStatus(100)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
	if event.type == pygame.KEYDOWN:
		if ( event.key == pygame.K_RIGHT):
			if (rightDrift.isActive() == False):
				rightDrift.start(speed[0])
			speed[0] = speed[0] + 1	
			print speed[0]
			
				
	

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
	rightDrift.changeVectorOrigSpeed()
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

    if (rightDrift.isActive()):
        rightDrift.wasteCycle()	
        if (rightDrift.isEnd()):
           speed[0] = rightDrift.orig_speed
           rightDrift.inactivate()
           print "volviendo " + str(speed)
