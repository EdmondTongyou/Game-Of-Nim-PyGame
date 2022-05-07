import pygame
import sys

pygame.init()
pygame.display.set_caption('Game of Nim')
flag = 0

# Variables
initial = True
active = True
userText = ''
xpos = 0
ypos = 0

# Fonts and Colors
test_font = pygame.font.Font('font/arial.ttf', 50)
author_font = pygame.font.Font('font/arial.ttf', 25)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive

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
input_surface = pygame.image.load('images/Textbox.png').convert()
text_surface = test_font.render(userText, True, 'Black')


# Rects for Surfaces
title_rect = title_surface.get_rect     (center = (400, 30))
author_rect = author_surface.get_rect   (center = (400, 100))
match_rect = match_surface.get_rect     (center = (400, 175))
button5_rect = button5_surface.get_rect (midleft = (50, 300))
button7_rect = button7_surface.get_rect (midleft = (300, 300))
button9_rect = button9_surface.get_rect (midleft = (550, 300))
input_rect = input_surface.get_rect     (topright = (750, 25))
text_rect = text_surface.get_rect       (center = (700, 25) )


# Draws and Updates the game
while True:
    # Event tracker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                userText = userText[:-1]
                text_surface = test_font.render(userText, True, 'Black')
            else:
                userText += event.unicode
                text_surface = test_font.render(userText, True, 'Black')

        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == pygame.MOUSEBUTTONUP:
            if button5_rect.collidepoint(event.pos):
                flag = 1
            elif button7_rect.collidepoint(event.pos):
                flag = 2
            elif button9_rect.collidepoint(event.pos):
                flag = 3
            elif input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
                pass
    
    if active:
        color = color_active
    else:
        color = color_passive

    # States of the Game
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

        # Initalizes Board and Draws current Board
        if initial == True:
            board = [0, 5, 3, 1]
            for index in range (0, len(board)):
                for count in range (0, board[index]):
                    match_rect = match_surface.get_rect     (topleft = (xpos, ypos))
                    resize_screen.blit(match_surface, match_rect)
                    xpos += 50
                xpos = 0
                ypos += 100
            ypos = 0
            resize_screen.blit(input_surface, input_rect)
            resize_screen.blit(text_surface, text_rect)
            screen.blit(pygame.transform.scale(resize_screen, screen.get_rect().size), (0, 0))
            pygame.display.flip()
            initial = False
        
        # Generates list of moves
        else:
            
            

            # Draws matches based off board
            for index in range (0, len(board)):
                for count in range (0, board[index]):
                    match_rect = match_surface.get_rect     (topleft = (xpos, ypos))
                    resize_screen.blit(match_surface, match_rect)
                    xpos += 50
                xpos = 0
                ypos += 100
            ypos = 0
            resize_screen.blit(input_surface, (input_rect.x+5, input_rect.y+5))
            screen.blit(pygame.transform.scale(resize_screen, screen.get_rect().size), (0, 0))
            
            pygame.display.flip()


    elif flag == 2:
        mouse_pos = pygame.mouse.get_pos()
        if initial == True:
            board = [7, 5, 3, 1]
            initial = False

    elif flag == 3:
        mouse_pos = pygame.mouse.get_pos()
        if initial == True:
            board = [9, 7, 5, 3, 1]
            initial = False

    pygame.display.update()