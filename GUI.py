import pygame as py
import Checker as ch
# Initialize Pygame
py.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set the dimensions of the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

# Set the size of the squares on the board
SQUARE_SIZE = 75

# Create the Pygame window
screen = py.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
py.display.set_caption("Checkers")

# Define a function to draw the game board
def draw_board():
    for row in range(8):
        for column in range(8):
            if (row + column) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            py.draw.rect(screen, color, [column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])

# Define a function to draw a checker piece
def draw_piece(row, column, color):
    py.draw.circle(screen, color, [(column * SQUARE_SIZE) + (SQUARE_SIZE // 2), (row * SQUARE_SIZE) + (SQUARE_SIZE // 2)], (SQUARE_SIZE // 2) - 10)

# Define the game board state
board = [
    [0, 'R', 0, 'R', 0, 'R', 0, 'R'],
    ['R', 0, 'R', 0, 'R', 0, 'R', 0],
    [0, 'R', 0, 'R', 0, 'R', 0, 'R'],
    ['-', 0, '-', 0, '-', 0, '-', 0],
    [0, '-', 0, '-', 0, '-', 0, '-'],
    ['B', 0, 'B', 0, 'B', 0, 'B', 0],
    [0, 'B', 0, 'B', 0, 'B', 0, 'B'],
    ['B', 0, 'B', 0, 'B', 0, 'B', 0]
]

#############
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = py.font.Font('freesansbold.ttf', 40)
text = font.render('Welcome', True, white)
textRect = text.get_rect()
textRect.midbottom=(WINDOW_WIDTH//2,WINDOW_HEIGHT-30-15)
display_surface = py.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# Game loop
running = True
while running:
    

    tempboard=ch.Board
    depth=5
    
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    display_surface.blit(text, textRect)

    # Draw the game board
    draw_board()
    # text = font.render('AI play ...', True, white)
    # textRect = text.get_rect()
    # textRect.midbottom=(X//2,Y-10-15)
    # display_surface.blit(text, textRect)
    # Draw the checker piecesd
    for row in range(8):
        for column in range(8):
            if board[row][column] == 'R':
                draw_piece(row, column, RED)
            elif board[row][column] == 'B':
                draw_piece(row, column, BLUE)
    
    while ch.Winner=='R' and tempboard != None:
        text = font.render('Computer plays ...', True, white)
        textRect = text.get_rect()
        textRect.midbottom=(WINDOW_WIDTH//2,WINDOW_HEIGHT-10-15)
        display_surface.blit(text, textRect)
        tempboard = ch.minmax(tempboard,depth,'B')
        if tempboard !=[]:
            ch.Assign(tempboard)
            ch.print_grid(tempboard)
        else:
            break
    ###########################
        print("----------------------------")
    ###########################
        if ch.Winner=='B' and tempboard != None:
            text = font.render('AI plays ...', True, white)
            textRect = text.get_rect()
            textRect.midbottom=(WINDOW_WIDTH//2,WINDOW_HEIGHT-10-15)
            display_surface.blit(text, textRect)
            tempboard = ch.get_child_by_random(tempboard,'B')
            if tempboard != None:
               ch.Assign(tempboard)
               ch.print_grid(tempboard)
            else:
                break
    ###########################
        print("----------------------------")
    ###########################
    if tempboard == None:
        print("Draw")
    #elif ch.utility(tempboard) == 20:
     #   print("B win")
    #else:
     #   print("R win")

    py.display.update()

# Quit Pygame
py.quit()