import sys
import pygame 
from init import create_minesweeper_image

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Buscaminas")

# Definir botones fuera de la función draw_menu()
button_5x5 = pygame.Rect(50, 120, 100, 50)
button_10x10 = pygame.Rect(150, 120, 100, 50)
button_15x15 = pygame.Rect(250, 120, 100, 50)
button_exit = pygame.Rect(150, 200, 100, 50)

def draw_menu():
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 40)

    # Texto del juego
    text = font.render("Buscaminas", True, BLACK)
    screen.blit(text, (150, 50))

    # Botón para cerrar
    pygame.draw.rect(screen, BLACK, (370, 10, 20, 20))  # x, y, width, height

    # Botones de tamaño
    pygame.draw.rect(screen, BLACK, button_5x5)
    text_5x5 = font.render("5x5", True, WHITE)
    screen.blit(text_5x5, (75, 135))

    pygame.draw.rect(screen, BLACK, button_10x10)
    text_10x10 = font.render("10x10", True, WHITE)
    screen.blit(text_10x10, (160, 135))

    pygame.draw.rect(screen, BLACK, button_15x15)
    text_15x15 = font.render("15x15", True, WHITE)
    screen.blit(text_15x15, (260, 135))

    # Botón de salir
    pygame.draw.rect(screen, BLACK, button_exit)
    text_exit = font.render("Salir", True, WHITE)
    screen.blit(text_exit, (180, 215))

    pygame.display.update()

def main_menu():
    while True:
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 370 <= mouse_pos[0] <= 390 and 10 <= mouse_pos[1] <= 30:  # Botón cerrar
                    pygame.quit()
                    sys.exit()
                elif button_5x5.collidepoint(mouse_pos):  # Botón 5x5
                    start_game(5, 5)
                elif button_10x10.collidepoint(mouse_pos):  # Botón 10x10
                    start_game(10, 10)
                elif button_15x15.collidepoint(mouse_pos):  # Botón 15x15
                    start_game(15, 15)
                elif button_exit.collidepoint(mouse_pos):  # Botón Salir
                    pygame.quit()
                    sys.exit()

def start_game(rows, cols):
    main_menu()
    pass

if __name__ == "__main__":
    main_menu()
