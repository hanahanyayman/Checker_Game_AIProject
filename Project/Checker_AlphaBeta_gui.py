import pygame, sys, time
from pygame.locals import *
import AlphaBeta as ch

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
RED1 = (255, 255,0)
BLUE = (0, 0, 255)
BLUE1 = (0, 255, 255)

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

SQUARE_SIZE = 75

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Checkers")

def draw_board():
    for row in range(8):
        for column in range(8):
            if (row + column) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, color, [column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])

def draw_piece(row, column, color):
    pygame.draw.circle(screen, color, [(column * SQUARE_SIZE) + (SQUARE_SIZE // 2), (row * SQUARE_SIZE) + (SQUARE_SIZE // 2)], (SQUARE_SIZE // 2) - 10)

white = (255, 255, 255)
font = pygame.font.Font('freesansbold.ttf', 40)
text = font.render('Welcome', True, white)
textRect = text.get_rect()
textRect.midbottom=(WINDOW_WIDTH//2,WINDOW_HEIGHT-30-15)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

ev = pygame.event.get()
clock = pygame.time.Clock()

draw_board()
for row in range(8):
    for column in range(8):
        if ch.Board[row][column] == 'R':
           draw_piece(row, column, RED)
        elif ch.Board[row][column] == 'B':
            draw_piece(row, column, BLUE)
tempboard=ch.Board
ch.depth=3
handled = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if pygame.mouse.get_pressed() and not handled and ch.utility(tempboard,'R') == 0 and tempboard != None:
        text = font.render('Computer plays ...', True, white)
        textRect = text.get_rect()
        textRect.midbottom=(WINDOW_WIDTH//2,WINDOW_HEIGHT-10-15)
        display_surface.blit(text, textRect)
        tempboard = ch.AlphaBeta(tempboard,ch.depth,'B',float('-inf'),float('inf'))
        if tempboard != []:
            ch.Assign(tempboard)
            for row in range(8):
                for column in range(8):
                    if tempboard[row][column] == 'R':
                         draw_piece(row, column, RED)
                    elif tempboard[row][column] == 'KR':
                         draw_piece(row, column, RED1)
                    elif tempboard[row][column] == 'B' :
                         draw_piece(row, column, BLUE)
                    elif tempboard[row][column] == 'KB':
                        draw_piece(row, column, BLUE1)
                    elif tempboard[row][column] == '-':
                        draw_piece(row,column,BLACK)
            handled=True
        else:
            break
    elif pygame.mouse.get_pressed()and handled  and ch.utility(tempboard,'B') == 0 and tempboard != None:
            time.sleep(3)
            text = font.render('AI plays ...', True, white)
            textRect = text.get_rect()
            textRect.midbottom=(WINDOW_WIDTH//2,WINDOW_HEIGHT-10-15)
            display_surface.blit(text, textRect)
            tempboard = ch.get_child_by_random(tempboard,'R')
            if tempboard != []:
               ch.Assign(tempboard)
               for row in range(8):
                    for column in range(8):
                        if tempboard[row][column] == 'R':
                          draw_piece(row, column, RED)
                        elif tempboard[row][column] == 'KR':
                          draw_piece(row, column, RED1)
                        elif tempboard[row][column] == 'B' :
                          draw_piece(row, column, BLUE)
                        elif tempboard[row][column] == 'KB':
                          draw_piece(row, column, BLUE1)
                        elif tempboard[row][column] == '-':
                          draw_piece(row,column,BLACK)
               handled=False
            else:
                break
    pygame.display.flip()
  
if tempboard == None:
    text = font.render('Draw !', True, white)
    textRect = text.get_rect()
    textRect.midbottom=(WINDOW_WIDTH//2,WINDOW_HEIGHT-10-15)
    display_surface.blit(text, textRect)
elif ch.utility(tempboard,'B') == 20:
    text = font.render('AI agent win', True, white)
    textRect = text.get_rect()
    textRect.midbottom=(WINDOW_WIDTH//2,WINDOW_HEIGHT-10-15)
    display_surface.blit(text, textRect)
else:
    text = font.render('Computer win', True, white)
    textRect = text.get_rect()
    textRect.midbottom=(WINDOW_WIDTH//2,WINDOW_HEIGHT-10-15)
    display_surface.blit(text, textRect)

pygame.quit()
