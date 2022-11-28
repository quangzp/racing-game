import time
class GameInfo:
    ROUND = 3
    def __init__(self,maps,round = 1):
        self.maps = maps
        self.round = round
        self.started = False
        self.round_start_time = 0
        self.player1 = 0
        self.player2 = 0
    
    def next_round(self):
        self.round +=1
        self.started = False
        
    def win(self,player):
        if player == 1:
            self.player1+=1
        else:
            self.player2+=1
    
    def reset(self):
        self.round = 1
        self.started = False
        self.player1 = 0
        self.player2 = 0
    
    def game_finished(self):
        return self.round > self.ROUND
    
    def start_round(self):
        self.started = True
        self.round_start_time = time.time()
    
    def get_round_time(self):
        if not self.started:
            return 0
        return round(time.time() - self.round_start_time)