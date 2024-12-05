def factorial(n):
    fac= 1
    for i in range(1,n+1):
        fac= fac*i
    return fac

import random
def math_challenge_factorial():
    n=0
    n= random.randint(1,10)
    ans= factorial(n)
    print("Math Challenge: Calculate the factorial of", n, "\n" )
    num= int(input("Your answer: \n"))
    if num == ans:
        print("Correct! You win a key")
    else:
        print("Incorrect, better luck next time...")



def solve_linear_equation():
    a= random.randint(1,10)
    b= random.randint(1,10)
    x= -b/a
    return a,b, x

def math_challenge_equation():
    solve_linear_equation()
    print("Math Challenge: Solve the equation", a,"x+", b,"=0")




