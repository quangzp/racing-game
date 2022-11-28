import pygame,math
from maps import *
from utils import *
from game_info import *
class PlayerCar:
    def __init__(self,img,max_vel,rotation_vel,map,type):
        self.img = img
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.base_map = map
        self.map = map
        self.acceleration = 0.1
        self.type = type
        self.x, self.y = self.set_position()
    
    def rotate(self,left=False,right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel		
    def draw(self,win):
        blit_rotate_center(win,self.img,(self.x,self.y),self.angle)
        
    def set_position(self):
        self.angle = self.map.angle_car
        self.vel = 0
        if self.angle == 90:
            print("a")
            self.x = self.map.finish_position[0] - 30
            self.y = self.map.finish_position[1] + (self.type - 1) * 40 + 10
        else:
            self.x = self.map.finish_position[0] + (self.type - 1) * 40
            self.y = self.map.finish_position[1] - 10
        return (self.x, self.y)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration , self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration , -self.max_vel/2)
        self.move()
    def move(self):
        radians = math.radians(self.angle)	
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.y -= vertical
        self.x -= horizontal
    
    def collide(self,mask,x=0,y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        point = mask.overlap(car_mask, offset)	
        return point

    def next_round(self,map):
        self.map = map
        self.set_position()
        
    def reset(self):
        self.map = self.base_map
        self.set_position()
    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration/2,0)
        self.move()
    
    def bounce(self):
        self.vel = -self.vel/2
        self.move()

def move_player(player_car1,player_car2):
    keys = pygame.key.get_pressed()
    moved1 = False
    moved2 = False
    
    if keys[pygame.K_a]:
        player_car1.rotate(left=True)
    if keys[pygame.K_d]:
        player_car1.rotate(right=True)
    if keys[pygame.K_w]:
        moved1 = True
        player_car1.move_forward()
    if keys[pygame.K_s]:
        moved1 = True
        player_car1.move_backward()
    if not moved1:
        player_car1.reduce_speed()
        
    if keys[pygame.K_LEFT]:
        player_car2.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        player_car2.rotate(right=True)
    if keys[pygame.K_UP]:
        moved1 = True
        player_car2.move_forward()
    if keys[pygame.K_DOWN]:
        moved1 = True
        player_car2.move_backward()
    if not moved2:
        player_car2.reduce_speed()
    
def handle_collision(player_car, map,game_info, WIN, MAIN_FONT):
    if player_car.collide(map.track_border_mask) != None:
        player_car.bounce()

    player_finish_poi_collide = player_car.collide(map.finish_mask, *map.finish_position)
    if player_finish_poi_collide != None:
        print(player_finish_poi_collide)
        if player_finish_poi_collide[map.finish_dimension] == map.finish_collision_val:
            player_car.bounce()
        else:
            blit_text_center(WIN, MAIN_FONT, f"Player {player_car.type} win!")
            pygame.display.update()
            pygame.time.wait(5000)
            game_info.win(player_car.type)
            game_info.next_round()
            