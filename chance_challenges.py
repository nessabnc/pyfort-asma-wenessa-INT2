import random
import time

def shell_game():
    l = []
    l = ['A', 'B','C']
    b= False
    attempt= 2
    print("Welcome to the shell game!\n", " In this game, you will need to choose between three shells named A, B and C.\n", " Under one of them, you may find a key. You will have two chance to select the correct shell that contains the key. Good luck!")
    print(l)
    for i in range(2):
       if b == False and attempt > 0:
           x = random.randint(0, 2)
           key = l[x]
           print("You have", attempt, "attempt left\n" )
           ans= str(input("Enter your choice:\n"))
           ans = ans.upper()
           if ans == key:
               print("Congratulations! You have found the key.\n")
               b = True
               return True
           else:
               attempt -=1
               print("You have selected the wrong shell\n")
               if attempt > 0:
                   print("You have been unsuccessful in this attempt\n")
               else:
                   print("You have lost, the key was under the", key, "shell\n")
                   return False


def roll_dice_game():
    attempt = 3
    a= False
    for i in range(3):
        if a == False and attempt >= 0:
           a= random.randint(1,5)
           b= random.randint(1,5)
           input("Press enter to roll the dice")
           t1= (a,b)
           time.sleep(1)
           print("You have rolled:", a,  "and", b)
           time.sleep(1)
           if 6 in t1:
               print("Congratulations! You have won the game and received a key.\n")
               a = True
               return True
           else:
               print("It is the game master's turn")
               x= random.randint(1,5)
               y= random.randint(1,5)
               t2=(x,y)
               time.sleep(1)
               print("The game master has rolled:", x, "and", y, "\n")
               time.sleep(1)
               attempt -=1
               if 6 in t2:
                   print("The game master has won the game, you have lost. Better luck next time!\n")
                   return False
               else:
                   a = False
    if attempt == 0:
        print("No player managed to score a 6 after three attempts, therefore it is a draw\n")
        return False


def chance_challenges():
    challenges = [shell_game, roll_dice_game]
    challenge= random.choice(challenges)
    print(challenge())

shell_game()
roll_dice_game()
chance_challenges()










    
    


