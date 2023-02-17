import pygame
from random import randint

# Functions for determining if a point is inside a polygon.
def is_between(value, y1, y2):
	if ((y1 > y2 and y1 >= value > y2) or
		y2 >= value > y1):
		return True
	return False

def calc_intersection(point, side_a, side_b):
	m = (side_b[1]-side_a[1])/(side_b[0]-side_a[0])
	x = ((point[1]-side_a[1])/m) + side_a[0]
	y = point[1]
	return (x, y)

def is_inside(point, polygon):
	count = 0
	for i in range(0, len(polygon)):
		a = polygon[i-1]
		b = polygon[i]
		if (a[1] != b[1] and
			is_between(point[1], a[1], b[1])):
			intersection = calc_intersection(point, a, b)
			if intersection[0] >= point[0]:
				count += 1
	if count % 2 == 0:
		return False
	return True


# The main program loop.
def main():
	pygame.init()
	WIDTH, HEIGHT = 500, 500
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()

	bg = pygame.Surface((WIDTH, HEIGHT))
	bg.fill((20,20,20))

	poly = [(250, 100), (400, 200), (350, 360),
				(150, 360), (100, 200)]

	random_points = []
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		# Displaying the background surface.
		screen.blit(bg, (0, 0))

		# 
		for point in random_points:
			if is_inside(point, poly):
				pygame.draw.circle(screen, (255,50,50), point, 2)
			else:
				pygame.draw.circle(screen, (255,255,100), point, 2)

		# Draw polygon.
		for x in range(0, len(poly)):
			pygame.draw.aaline(screen, (255,255,255), poly[x], poly[x-1])

		x = randint(0, WIDTH)
		y = randint(0, HEIGHT)
		random_points.append((x,y))

		pygame.display.update()
		clock.tick(60)


if __name__ == '__main__':
	main()
