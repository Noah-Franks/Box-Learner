import pygame

black    =    (   0,   0,   0)
lGrey    =    ( 140, 140, 140)
white    =    ( 255, 255, 255)
blue     =    (   0,   0, 255)
red      =    ( 255,   0,   0)

pygame.init()

sWidth = 800
sHeight = 600
GridSize = 64

screen = pygame.display.set_mode((sWidth, sHeight))
clock = pygame.time.Clock()

Map = []
for x in range(sWidth // GridSize + 1):
	Map.append([])
	for y in range(sHeight // GridSize + 1):
		Map[x].append(0)

def new_grid(size):
	global GridSize, Map

	for x in range(sWidth // size + 1):
		if x >= sWidth // GridSize + 1:
			Map.append([])
			for y in range(sHeight // GridSize + 1):
				Map[x].append(0)

	for x in range(sWidth // size + 1):
		for y in range(sHeight // size + 1):
			if y >= sHeight // GridSize + 1:
				Map[x].append(0)

	GridSize = size



ant_position = (sWidth // GridSize // 2, sHeight // GridSize // 2)
ant_direction = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)

	if ant_direction % 4 == 0:   # Move the ant based on it's direction
		ant_position = (ant_position[0] + 1, ant_position[1])
	elif ant_direction % 4 == 1:
		ant_position = (ant_position[0], ant_position[1] - 1)
	elif ant_direction % 4 == 2:
		ant_position = (ant_position[0] - 1, ant_position[1])
	elif ant_direction % 4 == 3:
		ant_position = (ant_position[0], ant_position[1] + 1)

	try:
		Map[ant_position[0]][ant_position[1]]
	except IndexError:
		new_grid(GridSize // 2)
	if Map[ant_position[0]][ant_position[1]] != 1:
		Map[ant_position[0]][ant_position[1]] = 1
		ant_direction += 1
	else:
		Map[ant_position[0]][ant_position[1]] = 2
		ant_direction -= 1


	# Drawing phase

	screen.fill(black)

	for x in range(sWidth // GridSize + 1):
		for y in range(sHeight // GridSize + 1):
			if (x, y) == ant_position:
				pygame.draw.rect(screen, white, [x * GridSize, y * GridSize, GridSize, GridSize])
				continue
			if Map[x][y] == 1:
				pygame.draw.rect(screen, red, [x * GridSize, y * GridSize, GridSize, GridSize])
			elif Map[x][y] == 2:
				pygame.draw.rect(screen, lGrey, [x * GridSize, y * GridSize, GridSize, GridSize])
		
	for i in range(sWidth // GridSize + 1):
		pygame.draw.line(screen, lGrey, [i * GridSize, 0], [i * GridSize, sHeight], 1)

	for i in range(sHeight // GridSize + 1):
		pygame.draw.line(screen, lGrey, [0, i * GridSize], [sWidth, i * GridSize], 1)

	pygame.display.flip()
	clock.tick(100)
