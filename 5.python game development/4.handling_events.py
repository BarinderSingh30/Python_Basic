import pygame 
pygame.init()

#creating window
gamewindow = pygame.display.set_mode((1200,500))        #tuple : width and height
pygame.display.set_caption("My First Game")     #game screen title

#game specific variables
exit_game = False           #will make it true in future so that user can quit the game
game_over = False           #will end the game if it over

#creating a game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()