import pygame
import random
from enum import Enum

from pygame.rect import Rect

pygame.init()
font=pygame.font.Font('arial.ttf',25)
class Point :
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self, other):
        if (isinstance(other, Point)):
            return self.x == other.x and self.y == other.y
        return False

class Direction(Enum) :
    RIGHT=1
    LEFT=2
    UP=3
    DOWN=4


BLOCK_SIZE=20
SPEED=15
WHITE = (255,255,255)
RED=(255,36,36)
NVGREEN1= (118, 185, 0)
NVGREEN2= (154,205,50)
BLACK=(0,0,0,)


class SnakeGame :
    def __init__(self,w=640,h=480):
        self.w=w
        self.h=h
        #init display
        self.display=pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption("snake")
        self.clock=pygame.time.Clock()
        
        #init game state
        self.direction=Direction.RIGHT
        self.head=Point(self.w/2,self.h/2)
        self.snake=[self.head,Point(self.head.x-BLOCK_SIZE,self.head.y),Point(self.head.x-2*BLOCK_SIZE,self.head.y)]
        self.score=0
        self.food=None
        self._place_food()
    
    def _place_food(self):
        x=random.randint(0,(self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y=random.randint(0,(self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food=Point(x,y)
        if self.food in self.snake:
            self._place_food()
    
    def _update_ui(self):
        self.display.fill(BLACK)
        for pt in self.snake:
            pygame.draw.rect(self.display,NVGREEN1,pygame.Rect(pt.x,pt.y,BLOCK_SIZE,BLOCK_SIZE))
            pygame.draw.rect(self.display,NVGREEN2,pygame.Rect(pt.x+BLOCK_SIZE/4,pt.y+BLOCK_SIZE/4,BLOCK_SIZE/2,BLOCK_SIZE/2))

        pygame.draw.rect(self.display,RED,pygame.Rect(self.food.x,self.food.y,BLOCK_SIZE,BLOCK_SIZE))
        text=font.render("Score : " + str(self.score),True,WHITE)
        self.display.blit(text,[0,0])
        pygame.display.flip()

    def _move(self,direction):
        x=self.head.x
        y=self.head.y
        if direction==Direction.RIGHT:
            x+=BLOCK_SIZE
        elif direction==Direction.LEFT:
            x-=BLOCK_SIZE
        elif direction==Direction.UP:
            y-=BLOCK_SIZE
        else:
            y+=BLOCK_SIZE

        self.head=Point(x,y)

    def _check(self):
        if self.head in self.snake[1:]:
            return True
        if(self.head.x<0 or self.head.x>self.w-BLOCK_SIZE):
            return True
        if(self.head.y<0 or self.head.y>self.h-BLOCK_SIZE):
            return True
        return False
        





    def play_step(self):
        #collect user ip
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.direction=Direction.LEFT
                elif event.key==pygame.K_RIGHT:
                    self.direction=Direction.RIGHT
                elif event.key==pygame.K_UP:
                    self.direction=Direction.UP
                elif event.key==pygame.K_DOWN:
                    self.direction=Direction.DOWN
        #move snake 
        self._move(self.direction)
        self.snake.insert(0,self.head)
        #check game over
        game_over=False
        if self._check():
            game_over=True
            return game_over,self.score

            # quit
        
        #place new food / move
        #print(self.food.x,self.food.y,self.head.x,self.head.y)
        if self.head.x==self.food.x and self.head.y==self.food.y:
            self.score+=1
            self._place_food()
        else:
            self.snake.pop()

        #update pygame ui and clk
        self._update_ui()
        self.clock.tick(SPEED)

        # return game over and score
        return game_over,self.score



if __name__== '__main__':
    game=SnakeGame()

    while True:
        game_over, score = game.play_step()
        if game_over == True:
            break
    
    print(f"final score={score}")
    
    pygame.quit()

