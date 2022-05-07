import sys
from search import *
from games import *
from game_of_nim import *
import pygame

pygame.init()
pygame.display.set_caption('Game of Nim')
clock = pygame.time.Clock()
flag = 0

# Fonts
test_font = pygame.font.Font('font/arial.ttf', 50)
author_font = pygame.font.Font('font/arial.ttf', 25)


# Screens and Surfaces
screen = pygame.display.set_mode((800, 400), pygame.RESIZABLE)
resize_screen = screen.copy()
backg_surface = pygame.image.load('images/Grey_Background.png').convert()

title_surface = test_font.render('Game of Nim', False, 'Black')
author_surface = author_font.render('by Edmond Tongyou', False, 'Black')

match_surface = pygame.image.load('images/Matchstick.png').convert_alpha()
button5_surface = pygame.image.load('images/Button_5.png').convert()
button7_surface = pygame.image.load('images/Button_7.png').convert()
button9_surface = pygame.image.load('images/Button_9.png').convert()


# Rects for Surfaces
title_rect = title_surface.get_rect     (center = (400, 30))
author_rect = author_surface.get_rect   (center = (400, 100))
match_rect = match_surface.get_rect     (center = (400, 175))
button5_rect = button5_surface.get_rect (midleft = (50, 300))
button7_rect = button7_surface.get_rect (midleft = (300, 300))
button9_rect = button9_surface.get_rect (midleft = (550, 300))


# Draws and Updates the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == pygame.MOUSEMOTION:
            if button5_rect.collidepoint(event.pos) and pygame.MOUSEBUTTONDOWN:
                flag = 1
    
    if flag == 0:
        mouse_pos = pygame.mouse.get_pos()
        resize_screen.blit(backg_surface,      (0, 0))
        resize_screen.blit(title_surface,      title_rect)
        resize_screen.blit(author_surface,     author_rect)
        resize_screen.blit(match_surface,      match_rect)
        resize_screen.blit(button5_surface,    button5_rect)
        resize_screen.blit(button7_surface,    button7_rect)
        resize_screen.blit(button9_surface,    button9_rect)
        screen.blit(pygame.transform.scale(resize_screen, screen.get_rect().size), (0, 0))
        pygame.display.flip()

    elif flag == 1:
        mouse_pos = pygame.mouse.get_pos()
        resize_screen.blit(backg_surface, (0, 0))
        screen.blit(pygame.transform.scale(resize_screen, screen.get_rect().size), (0, 0))
        pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

# Need to create initial board states for 1, 3, 5, 7, 9 board states
# Additionally need to create board states for 2, 4, 6, 8 depending on matches taken
# First idea is to create single match surface in left and have matches "spread" right from it
# Different for odd vs even number of matches
# i.e.
# [] vs 
# [] [] vs
# [] [] []