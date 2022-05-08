import pygame
import sys

pygame.init()
pygame.display.set_caption('Game of Nim')


# Variables
clock = pygame.time.Clock()
initial = True
active = False
aiMove = ''
userText = ''
turn = 0
xpos = 0
ypos = 0
flag = 0
board = list()
moves = list()

# Fonts and Colors
test_font = pygame.font.Font('font/arial.ttf', 50)
author_font = pygame.font.Font('font/arial.ttf', 25)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('Grey')
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
text_surface = test_font.render(userText, True, 'Black')


# Rects for Surfaces
title_rect = title_surface.get_rect     (center = (400, 30))
author_rect = author_surface.get_rect   (center = (400, 100))
match_rect = match_surface.get_rect     (center = (400, 175))
button5_rect = button5_surface.get_rect (midleft = (50, 300))
button7_rect = button7_surface.get_rect (midleft = (300, 300))
button9_rect = button9_surface.get_rect (midleft = (550, 300))
text_rect = text_surface.get_rect       (center = (650, 35) )

# Helper methods
def aiAction(board, move):
    pass

def playerAction(move):
    global moves
    global board
    move = eval(move)
    x = board[move[0]]
    if move not in moves:
        print("Not in moves")
        return

    # Sets deadStates based off board position - move made
    # Sets board as board position - move made    
    deadStates = move[1]
    board[move[0]] = board[move[0]] - move[1]
    
    # If deadStates is 0 then all moves for board position must be removed so x position gets moved
    # Checks if there is only 1 move and only removes that if that is the case
    if deadStates == 0:
        deadStates = move[1]
        x = (moves.index(move) - (moves.index(move) - deadStates - 2))
    if len(moves) == 1:
        moves.remove(moves[0])
    else:
        for index in range(0, deadStates):
            moves.remove(((move[0]), (x-index)))
    moves = moves
    board = board
    return board, moves

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
            elif event.key == pygame.K_RETURN:
                playerAction(userText)
                aiAction(aiMove)
            else:
                if len(userText) >= 6:
                    pass
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
            elif text_rect.collidepoint(event.pos):
                active = True
    
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
        pygame.draw.rect(resize_screen, color, text_rect)
        # Initalizes Board and Draws current Board
        if initial == True:
            board = [0, 5, 3, 1]
            for index in range(0, len(board)):
                x = index
                moves += ([((x, y)) for y in range(1, board[index] + 1)])
            for index in range (0, len(board)):
                for count in range (0, board[index]):
                    match_rect = match_surface.get_rect     (topleft = (xpos, ypos))
                    resize_screen.blit(match_surface, match_rect)
                    xpos += 50
                xpos = 0
                ypos += 100
            ypos = 0
            resize_screen.blit(text_surface, text_rect)
            text_rect.w = max(100, text_surface.get_width()+10)
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
            resize_screen.blit(text_surface, (text_rect.x+5, text_rect.y+5))
            text_rect.w = max(100, text_surface.get_width()+10)
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

    if len(moves) == 0:
        pass
    pygame.display.update()
    clock.tick(600)