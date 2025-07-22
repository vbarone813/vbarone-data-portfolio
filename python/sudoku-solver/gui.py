import sys
import pygame as pg
from solver import generate_random_grid, solve, valid
pg.init()

# Screen dimensions and setup
screen = pg.display.set_mode((750, 750))
pg.display.set_caption("Sudoku GUI")
font = pg.font.SysFont('times new roman', 60)

#colors
dimgray = pg.Color("dimgray")
white = pg.Color("white")
black = pg.Color("black")

# Sample Sudoku grid
grid = [
    [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
]
selected_cell = None 

def draw_background():
    screen.fill(white)
    pg.draw.rect(screen, dimgray, pg.Rect(50, 50, 650, 650), 5)
    
    grid_start = 55
    grid_end = 695
    cell_size = 72
    
    for i in range(1, 9):
        line_width = 2 if i % 3 else 5
        x = grid_start + i * cell_size 
        pg.draw.line(screen, dimgray, (x, grid_start), (x, grid_end), line_width)
        y = grid_start + i * cell_size
        pg.draw.line(screen, dimgray, (grid_start, y), (grid_end, y), line_width)

def draw_numbers():
    for row in range(9):
        for col in range(9):
            output = grid[row][col]
            if output != 0:  # Skip empty cells
                n_text = font.render(str(output), True, black)
                cell_center_x = 55 + col * 72 + 36
                cell_center_y = 55 + row * 72 + 36
                text_rect = n_text.get_rect(center=(cell_center_x, cell_center_y))
                screen.blit(n_text, text_rect)

def draw_selected_cell():
    if selected_cell: 
        row, col = selected_cell 
        cell_rect = pg.Rect(55 + col * 72, 55 + row * 72, 72, 72)
        pg.draw.rect(screen, "pink", cell_rect, 5)

def handle_mouse_clicks(x, y): 
    global selected_cell 
    col = (x - 55) // 72
    row = (y - 55) // 72
    if 0 <= row < 9 and 0 <= col < 9:
        selected_cell = (row, col)

def handle_keyboard_input(event):
    global grid 
    if selected_cell:
        row, col = selected_cell 
        if pg.K_1 <= event.key <= pg.K_9:
            num = event.key - pg.K_0 
            if valid(grid, num, (row, col)):  # Check if placing this number is valid
                grid[row][col] = num  # Only update the grid if valid
            else:
                print(f"Invalid move: {num} at ({row}, {col})")
        elif event.key == pg.K_0:  # Allow clearing a cell with the 0 key
            grid[row][col] = 0              

def handle_generate_grid(event):
    global grid
    if event.key == pg.K_g:
        grid = generate_random_grid(num_holes = 40)
    elif event.key == pg.K_b:
        grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]    


def solve_sudoku():
    if solve(grid):
        print("solved")
    else:
        print("no solution")    

def game_loop():
    global grid 
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                handle_mouse_clicks(*pg.mouse.get_pos())
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_g, pg.K_b):
                    handle_generate_grid(event)  
                elif event.key == pg.K_s:
                    solve_sudoku()    
                handle_keyboard_input(event)        

        draw_background()
        draw_numbers()
        draw_selected_cell()
        pg.display.flip()

    pg.quit()
    sys.exit()

# Start the game loop
game_loop()
