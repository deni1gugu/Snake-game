import pygame
import time
import random
import sys
            
            #игровое поле

pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255, 160, 16)
dis_width = 500
dis_height = 500
dis = pygame.display.set_mode((dis_width, dis_height))
sc = pygame.display.set_mode((dis_width, dis_height))
sc.fill((100, 150, 200))

 



pygame.display.set_caption('Snake game')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont('', 40, bold=True)
score_font = pygame.font.SysFont('', 40, bold=True)
 
def Your_score(score):
   pygame.display.set_caption('Snake game')
   value = score_font.render("Your score: " + str(score), True, orange)
   dis.blit(value, [0, 0])
 
def our_snake(snake_block, snake_list):
   for x in snake_list:
       pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
def message(msg, color):
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width / 6, dis_height / 3])
            
            #границы

def gameLoop():
   game_over = False
   game_close = False
   x1 = dis_width / 2
   y1 = dis_height / 2
   x1_change = 0
   y1_change = 0
   snake_List = []
   Length_of_snake = 1
   foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
   foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
   while not game_over:
       while game_close == True:
           dis.fill(black)
           message("You lost! Q-Exit, C-Restart", red)
           Your_score(Length_of_snake - 1)
          
           #управление
          
           pygame.display.update()
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_q:
                       game_over = True
                       game_close = False
                   if event.key == pygame.K_c:
                       gameLoop()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               game_over = True
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_a:
                   x1_change = -snake_block
                   y1_change = 0
               elif event.key == pygame.K_d:
                   x1_change = snake_block
                   y1_change = 0
               elif event.key == pygame.K_w:
                   y1_change = -snake_block
                   x1_change = 0
               elif event.key == pygame.K_s:
                   y1_change = snake_block
                   x1_change = 0
       if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
           game_close = True
       x1 += x1_change
       y1 += y1_change
       dis.fill(black)

            #еда для змейки
      
       pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
       snake_Head = []
       snake_Head.append(x1)
       snake_Head.append(y1)
       snake_List.append(snake_Head)
       if len(snake_List) > Length_of_snake:
           del snake_List[0]
       for x in snake_List[:-1]:
           if x == snake_Head:
               game_close = True
       our_snake(snake_block, snake_List)
       Your_score(Length_of_snake - 1)
       pygame.display.update()
       if x1 == foodx and y1 == foody:
           foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
           foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
           Length_of_snake += 1
       clock.tick(snake_speed)
   pygame.quit()
   quit()
gameLoop()
#endrrrr