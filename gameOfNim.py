import pygame
import sys
import random

pygame.init()
pygame.display.set_caption('Game of Nim')


# Variables
clock = pygame.time.Clock()
initial = True
active = False
aiMove = ''
userText = ''
victoryText = ''
turn = 0
xpos = 0
ypos = 0
flag = 0
board = list()
moves = list()

# Fonts and Colors
text_font = pygame.font.Font('font/arial.ttf', 50)
author_font = pygame.font.Font('font/arial.ttf', 25)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('Grey')
color = color_passive


# Screens and Surfaces
screen = pygame.display.set_mode((1600, 800), pygame.RESIZABLE)
resize_screen = screen.copy()
backg_surface = pygame.image.load('images/Grey_Background.png').convert()

title_surface = text_font.render('Game of Nim', False, 'Black')
author_surface = author_font.render('by Edmond Tongyou', False, 'Black')

match_surface = pygame.image.load('images/Matchstick.png').convert_alpha()
button5_surface = pygame.image.load('images/Button_5.png').convert()
button7_surface = pygame.image.load('images/Button_7.png').convert()
button9_surface = pygame.image.load('images/Button_9.png').convert()
text_surface = text_font.render(userText, True, 'Black')
victory_surface = text_font.render(victoryText, True, 'Black')


# Rects for Surfaces
title_rect = title_surface.get_rect     (center = (800, 60))
author_rect = author_surface.get_rect   (center = (800, 200))
match_rect = match_surface.get_rect     (center = (800, 350))
button5_rect = button5_surface.get_rect (midleft = (100, 600))
button7_rect = button7_surface.get_rect (midleft = (600, 600))
button9_rect = button9_surface.get_rect (midleft = (1100, 600))
text_rect = text_surface.get_rect       (center = (1100, 400))
victory_rect = victory_surface.get_rect (center = (1100, 600))


# Helper Functions
def aiAction():
    global board, moves, turn
    flag = True
    sum = 0
    for index in range(0, len(board)):
        sum += board[index]
    
    # Nim Sums are always Even therefore we can just check if the move selected is even or not
    while(flag):
        move = random.choice(moves)
        if sum % 2 == 0:
            if move[1] % 2 == 0:
                flag = False
        else:
            if move[1] % 2 != 0:
                flag = False
    x = board[move[0]]

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
    board = board
    moves = moves
    turn = 0
    return board, moves, turn

def playerAction(move):
    global board, moves, turn
    move = eval(move)
    x = board[move[0]]
    if move not in moves:
        print('Not in moves')
        return 'Redo'

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
    board = board
    moves = moves
    turn = 1
    return board, moves, turn

def displayBoard():
    global board, moves, xpos, ypos
    for index in range (0, len(board)):
        for count in range (0, board[index]):
            match_rect = match_surface.get_rect(topleft = (xpos, ypos))
            resize_screen.blit(match_surface, match_rect)
            xpos += 100
        xpos = 0
        ypos += 200
    ypos = 0
    resize_screen.blit(text_surface, (text_rect.x+5, text_rect.y-5))
    text_rect.w = max(125, text_surface.get_width()+10)
    resize_screen.blit(victory_surface, victory_rect)
    screen.blit(pygame.transform.scale(resize_screen, screen.get_rect().size), (0, 0))
    pygame.display.flip()
    board = board
    moves = moves
    xpos = xpos
    ypos = ypos
    return board, moves, xpos, ypos

def displayVictory():
    global victoryText, victory_surface, turn
    if turn == 0:
        victoryText = 'Player Wins!'
        victory_surface = text_font.render(victoryText, True, 'Black')
    else:
        victoryText = 'Computer Wins!'
        victory_surface = text_font.render(victoryText, True, 'Black')
    resize_screen.blit(text_surface, (text_rect.x+5, text_rect.y-5))
    text_rect.w = max(125, text_surface.get_width()+10)
    resize_screen.blit(victory_surface, victory_rect)
    screen.blit(pygame.transform.scale(resize_screen, screen.get_rect().size), (0, 0))
    pygame.display.flip()
    return victoryText


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
                text_surface = text_font.render(userText, True, 'Black')
            elif event.key == pygame.K_RETURN:
                if userText.isupper() == False and userText.islower() == False and len(userText) == 6 and eval(userText) in moves:
                    playerAction(userText)
                    if len(moves) != 0:
                        aiAction()
                    userText = ''
                    move = ''
                    text_surface = text_font.render(userText, True, 'Black')
                else:
                    pass
            else:
                if len(userText) >= 6:
                    pass
                else:
                    userText += event.unicode
                    text_surface = text_font.render(userText, True, 'Black')

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
            displayBoard()
            initial = False
        
        # Generates list of moves
        else:
            # Draws matches based off board
            displayBoard()


    elif flag == 2:
        mouse_pos = pygame.mouse.get_pos()
        resize_screen.blit(backg_surface, (0, 0))
        pygame.draw.rect(resize_screen, color, text_rect)
        # Initalizes Board and Draws current Board
        if initial == True:
            board = [7, 5, 3, 1]
            for index in range(0, len(board)):
                x = index
                moves += ([((x, y)) for y in range(1, board[index] + 1)])
            displayBoard()
            initial = False
        
        # Generates list of moves
        else:
            # Draws matches based off board
            displayBoard()

    elif flag == 3:
        mouse_pos = pygame.mouse.get_pos()
        resize_screen.blit(backg_surface, (0, 0))
        pygame.draw.rect(resize_screen, color, text_rect)
        # Initalizes Board and Draws current Board
        if initial == True:
            board = [9, 7, 5, 3, 1]
            for index in range(0, len(board)):
                x = index
                moves += ([((x, y)) for y in range(1, board[index] + 1)])
            displayBoard()
            initial = False
        
        # Generates list of moves
        else:
            # Draws matches based off board
            displayBoard()

    if len(moves) == 0 and flag != 0:
        if turn == 0:
            displayVictory()
        else:
            displayVictory()
    pygame.display.update()