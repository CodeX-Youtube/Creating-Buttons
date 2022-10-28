import pygame as pg

pg.init()

WIDTH, HEIGHT = 720, 480
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
buttons = []

fonts = {}
for i in range(1, 100):
	fonts[i] = pg.font.Font('font.otf', i)

class Button:
	def __init__(self, pos, color, color2, size, action_on_click, text=''):
		self.pos = pos
		self.color = color
		self.color2 = color2
		self.size = size
		self.text = text
		self.action_on_click = action_on_click
		buttons.append(self)

		self.zoom = 1

	def check_cursor(self):
		left = self.pos[0]-self.size[0]/2
		right = self.pos[0]+self.size[0]/2
		top = self.pos[1]-self.size[1]/2
		bottom = self.pos[1]+self.size[1]/2
		cursor = pg.mouse.get_pos()
		if cursor[0] >= left and cursor[0] <= right and cursor[1] >= top and cursor[1] <= bottom:
			return True
		else:
			return False

	def draw(self):
		image = pg.Surface((self.size[0], self.size[1]))
		if not self.check_cursor():
			draw_color = self.color2
			self.zoom += (1-self.zoom) * 0.1
		else:
			draw_color = self.color
			self.zoom += (1.2-self.zoom) * 0.1
		draw_size = [round(self.size[0]*self.zoom), round(self.size[1]*self.zoom)]
		image = pg.Surface(draw_size)
		image.fill(draw_color)
		text = fonts[draw_size[1]-5].render(self.text, False, (255, 255, 255))
		image.blit(text, (draw_size[0]/2-text.get_width()/2, draw_size[1]/2-text.get_height()/2))
		screen.blit(image, (self.pos[0]-image.get_width()/2, self.pos[1]-image.get_height()/2))

def end_window():
	global run
	run = False

Button([300, 50], (255, 100, 100), (150, 100, 100), [400, 60], None, text='RandomButton')
Button([400, 200], (255, 100, 255), (150, 100, 150), [200, 80], end_window, text='QUIT')

run = True
while run:
	clock.tick(60)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
		if event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:
				for button in buttons:
					if button.check_cursor():
						button.action_on_click()

	screen.fill((0, 0, 0))

	for button in buttons:
		button.draw()
	pg.display.update()

pg.quit()