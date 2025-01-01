import random

def display_grid():

    grid= [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    for i in range(3):
        space = ""
        for j in range(3):
            space=  space + grid[i][j] + "|"
        print(space)
        print("--------")

def check_victory(grid):
    a= 0
    b= 0
    for i in range(3):
        for j in range(3):







