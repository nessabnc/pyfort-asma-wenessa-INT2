import random

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
           print("You have", attempt, "attempt left" )
           ans= str(input("Enter your choice:"))
           ans = ans.upper()
           if ans == key:
               print("Congratulations! You have found the key.")
               b = True
               return True
           else:
               attempt -=1
               print("You have selected the wrong shell/n")
               if attempt > 0:
                   print("You have been unsuccessful in this attempt")
               else:
                   print("You have lost, the key was under the", key, "shell")
                   return False


def roll_dice_game():
    attempt = 3












    
    


