import pygame
from car import *

def draw(win,images,player_car1,player_car2,game_info,MAIN_FONT):
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