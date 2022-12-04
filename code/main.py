import pygame
from pygame import mixer
from utils import *
from car import *
from maps import *
from draw import *
from game_info import *

#for map 1
TRACK = pygame.image.load("images/duongdua.png")
TRACK_BORDER = pygame.image.load("images/vien.png")
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)

TRACK1 = pygame.image.load("images/track1.png")
TRACK_BORDER1 = pygame.image.load("images/track-border1.png")
TRACK_BORDER_MASK1 = pygame.mask.from_surface(TRACK_BORDER1)
FINISH_POSITION1 = (700, 590)
ANGLE_CAR1 = 90
FINISH_DIMENSION1 = 0
FINISH_COLLISION_VAL1 = 2

#for map 2
TRACK2 = pygame.image.load("images/track4.png")
TRACK_BORDER2 = scale_image(pygame.image.load("images/track-border4.png"),1) 
TRACK_BORDER_MASK2 = pygame.mask.from_surface(TRACK_BORDER2)
FINISH_POSITION2 = (650, 580)
ANGLE_CAR2 = 90
FINISH_DIMENSION2 = 0
FINISH_COLLISION_VAL2 = 2
#for map 3
TRACK3 = pygame.image.load("images/track5.png")
TRACK_BORDER3 = pygame.image.load("images/track-border5.png")
TRACK_BORDER_MASK3 = pygame.mask.from_surface(TRACK_BORDER3)
FINISH_POSITION3 = (700, 570)
ANGLE_CAR3 = 90
FINISH_DIMENSION3 = 0
FINISH_COLLISION_VAL3 = 2

RED_CAR = scale_image(pygame.image.load("images/red-car.png"), 0.06)
YELLOW_CAR = scale_image(pygame.image.load("images/yellow-car.png"), 0.06)
WHITE_CAR = scale_image(pygame.image.load("images/white-car.png"), 0.06)

WIDTH, HEIGHT = GRASS.get_width(), GRASS.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")
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
# map4 = Map(TRACK,TRACK_BORDER,(670,600),ANGLE_CAR1,FINISH_DIMENSION1,FINISH_COLLISION_VAL1)
game_info = GameInfo((map1,map2,map3))
player_car1 = PlayerCar(6, 6,map1, 1)
player_car2 = PlayerCar(6, 6,map1, 2)
while run:
    clock.tick(FPS)
    
    # while not game_info.started and game_info.round == 1:
    #     select_color_car(WIN,MAIN_FONT,player_car1,player_car2)
    player_car1.set_img(RED_CAR)
    player_car2.set_img(YELLOW_CAR)
    
    cur_map = game_info.maps[game_info.round - 1]
    draw(WIN, cur_map, player_car1, player_car2,game_info,MAIN_FONT)
    
    while not game_info.started:
        blit_text_center(WIN, MAIN_FONT, f"Press any key to start level {game_info.round}!")
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

    handle_collision(player_car1,cur_map,game_info,WIN, MAIN_FONT)
    handle_collision(player_car2,cur_map,game_info,WIN, MAIN_FONT)
    
    if not game_info.started and game_info.round <= game_info.ROUND:
        player_car1.next_round(game_info.maps[game_info.round-1])
        player_car2.next_round(game_info.maps[game_info.round-1])
    
    if game_info.game_finished():
        if game_info.player1 > game_info.player2:
            winner = 1
        else:
            winner = 2
        game_info.reset()
        player_car1.reset()
        player_car2.reset()
        draw(WIN, game_info.maps[0], player_car1, player_car2,game_info,MAIN_FONT)
        blit_text_center(WIN, MAIN_FONT, f"Player{winner} won the game!")
        pygame.display.update()
        pygame.time.wait(5000)
pygame.quit()
