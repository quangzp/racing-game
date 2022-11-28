import pygame
from pygame import mixer
from utils import *
from car import *
from maps import *
from draw import *
from game_info import *

GRASS = scale_image(pygame.image.load("images/grass.png"), 2.5)

FINISH = scale_image(pygame.image.load("images/finish.png"),0.1)
FINISH_MASK = pygame.mask.from_surface(FINISH)

#for map 1
TRACK1 = scale_image(pygame.image.load("images/track1.png"), 1)
TRACK_BORDER1 = scale_image(pygame.image.load("images/track-border1.png"), 1)
TRACK_BORDER_MASK1 = pygame.mask.from_surface(TRACK_BORDER1)
FINISH_POSITION1 = (700, 590)
ANGLE_CAR1 = 90
FINISH_DIMENSION1 = 0
FINISH_COLLISION_VAL1 = 1

#for map 2
TRACK2 = scale_image(pygame.image.load("images/track2.png"), 1)
TRACK_BORDER2 = scale_image(pygame.image.load("images/track-border2.png"), 1)
TRACK_BORDER_MASK2 = pygame.mask.from_surface(TRACK_BORDER2)
FINISH_POSITION2 = (900, 500)
ANGLE_CAR2 = 0
FINISH_DIMENSION2 = 1
FINISH_COLLISION_VAL2 = 1
#for map 3
TRACK3 = scale_image(pygame.image.load("images/track3.png"), 1)
TRACK_BORDER3 = scale_image(pygame.image.load("images/track-border3.png"), 1)
TRACK_BORDER_MASK3 = pygame.mask.from_surface(TRACK_BORDER3)
FINISH_POSITION3 = (350, 600)
ANGLE_CAR3 = 90
FINISH_DIMENSION3 = 0
FINISH_COLLISION_VAL3 = 1

RED_CAR = scale_image(pygame.image.load("images/redcar.png"), 0.06)
YELLOW_CAR = scale_image(pygame.image.load("images/yellowcar.png"), 0.06)

WIDTH, HEIGHT = TRACK1.get_width(), TRACK1.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")
pygame.font.init()
MAIN_FONT = pygame.font.SysFont("comicsans", 44)
FPS = 60
mixer.init()
mixer.music.load("Dreamers.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

run = True
clock = pygame.time.Clock()

map1 = Map(TRACK1,TRACK_BORDER1,FINISH_POSITION1,ANGLE_CAR1,FINISH_DIMENSION1,FINISH_COLLISION_VAL1)
map2 = Map(TRACK2,TRACK_BORDER2,FINISH_POSITION2,ANGLE_CAR2,FINISH_DIMENSION2,FINISH_COLLISION_VAL2)
map3 = Map(TRACK3,TRACK_BORDER3,FINISH_POSITION3,ANGLE_CAR3,FINISH_DIMENSION3,FINISH_COLLISION_VAL3)
game_info = GameInfo((map1,map2,map3))
player_car1 = PlayerCar(RED_CAR,6, 6,map1, 1)
player_car2 = PlayerCar(YELLOW_CAR,6, 6,map1, 2)
while run:
    clock.tick(FPS)
    
    new_map = game_info.maps[game_info.round - 1]
    
    draw(WIN, new_map.get_images(), player_car1, player_car2,game_info,MAIN_FONT)
    
    while not game_info.started:
        blit_text_center(
            WIN, MAIN_FONT, f"Press any key to start level {game_info.round}!")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                game_info.start_round()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    move_player(player_car1,player_car2)

    handle_collision(player_car1,map1,game_info,WIN, MAIN_FONT)
    handle_collision(player_car2,map1,game_info,WIN, MAIN_FONT)
    
    if not game_info.started:
        player_car1.next_round(game_info.maps[game_info.round-1])
        player_car2.next_round(game_info.maps[game_info.round-1])
    
    if game_info.game_finished():
        blit_text_center(WIN, MAIN_FONT, "You won the game!")
        pygame.time.wait(5000)
        game_info.reset()
        player_car1.reset()
        player_car2.reset()

pygame.quit()
