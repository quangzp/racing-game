import pygame

class Map:
    def __init__(self,track,track_border,finish_position,angle_car,finish_dimension,finish_collision_val):
        self.GRASS = pygame.image.load("images/grass.png")
        self.track = track
        self.track_position = (0,0)
        self.track_border = track_border
        self.border_position = (0,0)
        self.track_border_mask = pygame.mask.from_surface(track_border)
        self.finish = pygame.image.load("images/finish.png")
        self.finish_position = finish_position
        self.finish_mask = pygame.mask.from_surface(self.finish)
        self.angle_car = angle_car
        self.finish_dimension = finish_dimension
        self.finish_collision_val = finish_collision_val
    
    def get_images(self):
        return {    
            "grass" : (self.GRASS, (0, 0)),
            "track" : (self.track, self.track_position),
            "finish" : (self.finish, self.finish_position,self.angle_car), 
            "track_border" : (self.track_border, self.border_position)
            }  
    