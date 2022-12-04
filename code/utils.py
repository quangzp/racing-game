import pygame
from game_info import *

pygame.font.init()
def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def blit_text_center(win, font, text):
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width()/2 - render.get_width() /
                      2, win.get_height()/2 - render.get_height()/2))

def draw(win,map,player_car1,player_car2,game_info,MAIN_FONT):
	images = map.get_images()
	for k in images:
		val = images[k]
		if k == 'finish':
			blit_rotate_center(win,val[0], val[1], 90 - val[2])
		else:
			win.blit(val[0],val[1])
	level_text = MAIN_FONT.render(
        f"Round {game_info.round}", 1, (255, 255, 255))
	win.blit(level_text, (10, win.get_height() - level_text.get_height() - 70))

	time_text = MAIN_FONT.render(
        f"Time: {game_info.get_round_time()}s", 1, (255, 255, 255))
	win.blit(time_text, (10, win.get_height() - time_text.get_height() - 40))
    
	player_car1.draw(win)
	player_car2.draw(win)
	pygame.display.update()

    
            