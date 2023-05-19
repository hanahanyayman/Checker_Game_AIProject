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
    display_surface.blit(text, textRect)
    
    # Handle events
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
        elif event.type == py.MOUSEBUTTONDOWN:
            # Get the row and column of the clicked square
            current_player = 'B'
            pos = py.mouse.get_pos()
            col = pos[0] // 80
            row = pos[0] // 80
            if board[row][col] == 0:
                board[row][col] = current_player
                draw_board()
                # Switch players
                current_player = 'R' if current_player == 'B' else 'B'

            # Make the move and update the board
            ch.move_B(board,row,col)
            ch.Assign(board)
    # Draw the game board
    draw_board()

    # Draw the checker pieces
    for row in range(8):
        for column in range(8):
             if board[row][column] == 'R':
                     draw_piece(row, column, RED)
             elif board[row][column] == 'B':
                    draw_piece(row, column, BLUE)
             elif board[row][column] == 'KB':
                     draw_piece(row, column, BLUE)
             elif board[row][column] == 'KR':
                    draw_piece(row, column, RED)

    # Update the screen
    py.display.flip()
    py.display.update()

# Quit Pygame
py.quit()