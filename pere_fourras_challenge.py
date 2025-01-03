import json
import random


def load_riddles(file):
    with open(file, 'r') as f:
        riddles = json.load(f)
    return riddles


def pere_fourras_riddles(file):
    riddles = load_riddles(file)
    riddle = random.choice(riddles)
    attempts = 3

    print("Père Fourras challenges you with a riddle from " + riddle["emission"] + " (Show " + riddle["number"] + "):")
    print(riddle["question"])

    while attempts > 0:
        answer = input("Your answer: ").lower()

        if answer == riddle["answer"].lower():
            print("Correct! You've won a key!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print("Incorrect! You have " + str(attempts) + " attempts remaining.")
            else:
                print("Incorrect! The correct answer was: " + riddle["answer"])
                print("You have failed to win the key.")
                return False
pere_fouras_riddles("data/PFRiddles (1).json")
