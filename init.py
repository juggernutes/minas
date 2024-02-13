import sys
import pygame 
import random
import math
from img.image import create_minesweeper_image
from PIL import Image, ImageDraw  


pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Minesweeper')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)
cyan = (0, 255, 255)
orange = (255, 165, 0)
colors = [black, blue, green, red, purple, cyan, orange, gray]

# Fonts
font = pygame.font.SysFont('Arial', 20)
font_small = pygame.font.SysFont('Arial', 15)
font_big = pygame.font.SysFont('Arial', 40)

# Images
mine_img = pygame.image.load('img/mine.png')
flag_img = pygame.image.load('img/flag.png')
mine_img = pygame.transform.scale(mine_img, (20, 20))
flag_img = pygame.transform.scale(flag_img, (20, 20))

# Game variables
rows, cols, cell_size = 10, 10, 40
mines = 10
board = [[0 for _ in range(cols)] for _ in range(rows)]
revealed = [[False for _ in range(cols)] for _ in range(rows)]
flags = [[False for _ in range(cols)] for _ in range(rows)]
game_over = False
game_won = False
first_click = True
mines_left = mines
time = 0
time_text = font.render(f'Time: {time}', True, black)
mines_left_text = font.render(f'Mines: {mines_left}', True, black)

# Create minesweeper image
create_minesweeper_image(rows, cols, cell_size)

# Functions
def draw_board():
    screen.fill(white)
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, black, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, black, (0, y), (width, y))
    for row in range(rows):
        for col in range(cols):
            if revealed[row][col]:
                if board[row][col] == -1:
                    screen.blit(mine_img, (col * cell_size, row * cell_size))
                else:
                    text = font.render(str(board[row][col]), True, colors[board[row][col]])
                    screen.blit(text, (col * cell_size + 10, row * cell_size + 10))
            if flags[row][col]:
                screen.blit(flag_img, (col * cell_size, row * cell_size))
    if game_over:
        text = font_big.render('Game Over', True, red)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    elif game_won:
        text = font_big.render('You Win', True, green)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    screen.blit(time_text, (10, height - 30))
    screen.blit(mines_left_text, (width - 110, height - 30))
    pygame.display.update()

def reveal(row, col):
    if row < 0 or row >= rows or col < 0 or col >= cols or revealed[row][col]:
        return
    revealed[row][col] = True
    if board[row][col] == 0:
        for r in range(-1, 2):
            for c in range(-1, 2):
                reveal(row + r, col + c)

def count_mines(row, col):
    count = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            if row + r < 0 or row + r >= rows or col + c < 0 or col + c >= cols:
                continue
            if board[row + r][col + c] == -1:
                count += 1
    return count

def create_board():
    global board
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    for _ in range(mines):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while board[row][col] == -1:
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        board[row][col] = -1
        for r in range(-1, 2):
            for c in range(-1, 2):
                if row + r < 0 or row + r >= rows or col + c < 0 or col + c >= cols:
                    continue
                if board[row + r][col + c] != -1:
                    board[row + r][col + c] += 1

def game_over_screen():
    global game_over
    game_over = True
    for row in range(rows):
        for col in range(cols):
            revealed[row][col] = True
    draw_board()

def game_won_screen():
    global game_won
    game_won = True
    for row in range(rows):
        for col in range(cols):
            revealed[row][col] = True
    draw_board()

def check_win():
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != -1 and not revealed[row][col]:
                return
    game_won_screen()

def start_game(row, col):
    global first_click
    if first_click:
        create_board()
        first_click = False
        while board[row][col] != 0:
            create_board()
    reveal(row, col)
    check_win()
    draw_board()

# Main loop
running = True

while running:
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over or game_won:
                continue
            x, y = pygame.mouse.get_pos()
            col = x // cell_size
            row = y // cell_size
            if event.button == 1:
                if flags[row][col]:
                    continue
                if board[row][col] == -1:
                    game_over_screen()
                else:
                    start_game(row, col)
            elif event.button == 3:
                if revealed[row][col]:
                    continue
                flags[row][col] = not flags[row][col]
                if flags[row][col]:
                    mines_left -= 1
                else:
                    mines_left += 1
                mines_left_text = font.render(f'Mines: {mines_left}', True, black)
                draw_board()
    time_text = font.render(f'Time: {time}', True, black)
    time += 1
    fpsClock.tick(fps)
    pygame.display.update()
pygame.quit()

# Path: img/image.py

def create_minesweeper_image(rows, cols, cell_size):
    width = cols * cell_size
    height = rows * cell_size
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    # Dibujar las líneas verticales
    for x in range(0, width, cell_size):
        draw.line([(x, 0), (x, height)], fill="black")

    # Dibujar las líneas horizontales
    for y in range(0, height, cell_size):
        draw.line([(0, y), (width, y)], fill="black")

    # Guardar imagen
    img.save(f"minesweeper_{rows}x{cols}.png")
    img.show()

# Crear imágenes para tableros de 5x5, 10x10 y 15x15
create_minesweeper_image(5, 5, 40)  # Tamaño de celda: 40x40
create_minesweeper_image(10, 10, 30)  # Tamaño de celda: 30x30
create_minesweeper_image(15, 15, 20)  # Tamaño de celda: 20x20

#Path: img/__init__.py

