from PIL import Image, ImageDraw

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

"""# Crear imágenes para tableros de 5x5, 10x10 y 15x15
create_minesweeper_image(5, 5, 40)  # Tamaño de celda: 40x40
create_minesweeper_image(10, 10, 30)  # Tamaño de celda: 30x30
create_minesweeper_image(15, 15, 20)  # Tamaño de celda: 20x20"""
