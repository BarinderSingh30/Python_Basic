import pygame
import random

pygame.init()

#colours

white = (255,255,255)
red = (255,0,0)
black =(0,0,0)



screen_width = 900
screen_height = 600

gamewindow=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('SnakesWithHarry')
pygame.display.update()

#games specific varibales

exit_game =False
game_over = False

snake_x=45
snake_y=55
snake_size=15
food_size=15
init_velocity = 5
velocity_x =0
velocity_y =0
fps=60

food_x = random.randint(10,screen_width//2)
food_y = random.randint(10,screen_height//2)
score=0
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)

def text_score(text,color,x,y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow,color,snk_list,snake_size):

    for x,y in snk_list:
        pygame.draw.rect(gamewindow,black,[x,y,snake_size,snake_size])

snk_list = []
snk_length = 1



#game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True

        if event.type == pygame.KEYDOWN:

            if event.key ==pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y=0

            if event.key ==pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0

            if event.key ==pygame.K_DOWN:
                velocity_y =  init_velocity
                velocity_x= 0
                
            if event.key ==pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0

    snake_x += velocity_x
    snake_y +=velocity_y

    if abs(snake_x - food_x) < 15 and abs(snake_y-food_y)<15:
        food_x = random.randint(10,screen_width//2)
        food_y = random.randint(10,screen_height//2)
        score+=1
        snk_length +=5
        
      



    gamewindow.fill(white)
    text_score(f'score : {score*10}',red, 5, 5)

    pygame.draw.rect(gamewindow,red,[food_x,food_y,food_size,food_size])

    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list)>snk_length:
        del snk_list[0]
    plot_snake(gamewindow,black,snk_list,snake_size)

    # pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])

    pygame.display.update()

    clock.tick(fps)

pygame.quit()
quit()

        
