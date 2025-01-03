import time
def display_grid(grid):
    for i in range(3):
        space = "|"
        for j in range(3):
            space= space + grid[i][j] + "|"
        print(space)
        print("--------")

def check_victory(grid, symbol):
    a = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j]== symbol:
                a += 1
        if a != 3:
           a = 0
        else:
           return True


    a = 0
    for row in range(3):
        for col in range(3):
            if grid[row][col]== symbol:
                a += 1
        if a !=3:
            a=0
        else:
            return True

    a = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                if grid[i][j]== symbol:
                    a +=1
    if a == 3:
        return True

    a = 0
    for i in range(3):
            if grid[i][3 - i - 1]== symbol:
                a+= 1
    if a == 3:
        return True

    return False


def master_move(grid, symbol):
    for i in range(3):
        a= 0
        for j in range(3):
            if grid[i][j]== "X":
                a += 1
        if a == 2:
            for j in range(3):
                if grid[i][j]== " ":
                   t= (i, j)
                   return t

    for j in range(3):
        a= 0
        for i in range(3):
            if grid[j][i]== "X":
                a += 1
        if a == 2:
            for i in range(3):
                if grid[j][i]== " ":
                    t=(j, i)
                    return t

    a = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                if grid[i][j] == "X":
                    a += 1
                if a == 2:
                    for x in range(3):
                        for y in range(3):
                            if x == y:
                                if grid[x][y]== " ":
                                    t= (x, y)
                                    return t




    a = 0
    for i in range(3):
        if grid[i][3 - i - 1] == "X":
            a += 1
        if a == 2:
            for j in range(3):
                if grid[j][3-j-1]== " ":
                    t=(j, (3-j-1))
                    return t

    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                t=(i, j)
                return t







def player_turn(grid):
    while True:
       symbol = "X"
       i = int(input("In which row would you like to place your symbol?"))
       j = int(input("In which column would you like to place your symbol?"))
       if grid[i-1][j-1]== symbol or grid[i-1][j-1]== "O":
          print("That place is already occupied, try again.")
       else:
          grid[i-1][j-1] = symbol
          break


def master_turn(grid):
    move = master_move(grid, "O")
    grid[move[0]][move[1]] = "O"




def full_grid(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j]== " ":
                return False
    return True



def check_result(grid):
    if full_grid(grid) == True or check_victory(grid, symbol)== True :
        return True
    else:
        return False

def tic_tac_toe():
    grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print("Welcome to tic-tac-toe against the game master!")
    print("To play enter your coordinates in the form row,column ")
    for i in range(4):
       player_turn(grid)
       display_grid(grid)
       symbol = "X"
       if check_result(grid)== True:
           print("Congrats, you have won!")
       else:
          print("It is the game master's turn.")
          time.sleep(1)
          master_move(grid, "O")
          master_turn(grid)
          display_grid(grid)
          symbol = "O"
          if check_result(grid)== True:
              print("The game master has won!")






tic_tac_toe()







































