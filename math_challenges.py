import random

def factorial(n):
    fac= 1
    for i in range(1,n+1):
        fac= fac*i
    return fac


def math_challenge_factorial():
    n=0
    n= random.randint(1,10)
    ans= factorial(n)
    print("Math Challenge: Calculate the factorial of", n, "\n" )
    num= int(input("Your answer: \n"))
    if num == ans:
        print("Correct! You win a key")
        return True
    else:
        print("Incorrect, better luck next time...")
        return False



def solve_linear_equation():
    a= random.randint(1,10)
    b= random.randint(1,10)
    x= -b/a
    return a,b, x

def math_challenge_equation():
    a, b, x = solve_linear_equation()
    print("What is", a, "x+", b)
    r= f"{-b}/{a}"
    z=str(int(-b/a))
    t= input("Enter your answer: \n")
    if t==r or t==z:
        print("Correct! You win a key")
        return True
    else :
        print("Incorrect")
        return False


def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    else :
        i = 3
        while i*i<=n:
            if n%i==0:
                return False
            else :
                i +=2
        return True

def nearest_prime(n):
    while not is_prime(n):
        n +=2
    return n


def math_challenge_prime():
    a= random.randint(10,20)
    answer= int(input("Enter the prime number closest to" + ' '+ str(a)))
    n = nearest_prime(answer)
    if answer == n:
        print("Correct! You win a key")
        return True
    else :
        print("Incorrect")
        return False

def math_challenge():
    challenges= [math_challenge_prime, math_challenge_factorial]
    challenge= random.choice(challenges)
    print(challenge())





















