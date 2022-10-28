import pygame as pg

pg.init()

WIDTH = 720
HEIGHT = 480
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

buttons = []

fonts = {}
for i in range(1, 100):
	fonts[i] = pg.font.Font('font.otf', i)

class Button:
	def __init__(self, color, size, pos, text, function_when_click):
		self.size = size
		self.color = color
		self.text = text
		self.pos = pos
		self.function_when_click = function_when_click

		self.zoom = 1

		buttons.append(self)

	def mouse_touching(self):
		mouse_pos = pg.mouse.get_pos()
		if mouse_pos[0] >= self.pos[0]-self.size[0]/2 and mouse_pos[0] <= self.pos[0]+self.size[0]/2:
			if mouse_pos[1] >= self.pos[1]-self.size[1]/2 and mouse_pos[1] <= self.pos[1]+self.size[1]/2:
				return True
		return False

	def draw(self):
	
		if self.mouse_touching():
			self.zoom += (1.5-self.zoom)*0.2
		else:
			self.zoom += (1-self.zoom)*0.2

		image = pg.Surface([round(self.size[0]*self.zoom), round(self.size[1]*self.zoom)])
		image.fill(self.color)

		text_img = fonts[round(self.size[1]*self.zoom)-4].render(self.text, False, (255, 255, 255))
		image.blit(text_img, (image.get_width()/2-text_img.get_width()/2, image.get_height()/2-text_img.get_height()/2))

		drawpos = [self.pos[0]-image.get_width()/2, self.pos[1]-image.get_height()/2]
		screen.blit(image, drawpos)
def close_window():
	global run 
	run = False
def say_hi():
	print('hi')
Button((100, 100, 100), [50, 50], [50, 50], 'Hi', None)
Button((100, 150, 100), [75, 50], [100, 150], 'Hi', say_hi)
Button((100, 100, 100), [50, 50], [50, 250], 'Hi', None)
Button((100, 100, 100), [50, 50], [150, 350], 'Hi', None)
Button((255, 100, 100), [100, 50], [400, 400], 'Bye', close_window)


run = True
while run:
	clock.tick(60)
	fps = clock.get_fps()

	pg.display.set_caption('Tutorial - {:.2f}FPS'.format(fps))

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
		if event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:
				for b in buttons:
					if b.mouse_touching():
						if b.function_when_click != None:
							b.function_when_click()

	screen.fill((0, 0, 0))
	for b in buttons: b.draw()

	pg.display.update()

pg.quit()