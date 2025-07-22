import random 

def valid(bo, num, pos):
    row, col = pos 
    #check the row
    for i in range(len(bo[0])):
        if bo[row][i] == num and col != i:
            return False
    #check the column     
    for i in range(len(bo)):
        if bo[i][col] == num and row != i:
            return False   
    #check the box 
    row, col = pos
    box_x = (row // 3) * 3
    box_y = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if bo[box_x + i][box_y + j] == num and (box_x + i, box_y + j) != pos:
                return False 

    return True  

def generate_random_grid(num_holes=40):
    def fill_grid(grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    random.shuffle(numbers)
                    for num in numbers:
                        if valid(grid, num, (row, col)):
                            grid[row][col] = num
                            if fill_grid(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    grid = [[0] * 9 for _ in range(9)]
    numbers = list(range(1, 10))
    fill_grid(grid)  # Fill grid completely

    for _ in range(num_holes):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while grid[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        grid[row][col] = 0
    return grid

board = generate_random_grid(num_holes = 40)

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(bo[0])): # row 0 is why we add that [0]
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="") 

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #(row, column)

    return None        

def solve(bo):
    #base case: what else the recursive algorithm 
    find = find_empty(bo)
    if not find:
        return True #solution
    else: 
        row, col = find 

    for i in range (1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True 
            
            bo[row][col] = 0 

    return False    


print("              ")
print_board(board)
solve(board)
print("              ")
print("solution:")
print_board(board)

