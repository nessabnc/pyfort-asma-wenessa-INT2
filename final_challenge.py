import json
import random

def treasury_room(file_path):
    tv_game = {}
    show = {}
    clues = []
    year = ""
    code_word = ""
    attempts = 3
    answer_correct = False

    file = open(file_path, 'r')
    tv_game = json.load(file)
    file.close()

    available_years = list(tv_game.keys())
    year = random.choice(available_years)

    programs = tv_game.get(year, [])
    if len(programs) == 0:
        print("No programs available for the selected year:", year)
        return

    show = random.choice(programs)

    clues = show.get('clues', [])
    code_word = show.get('code_word', "").strip().upper()

    if len(clues) < 3 or not code_word:
        print("Invalid data for the selected program. Please check your JSON file.")
        return

    print("Welcome to the Treasury Room!")
    print("Year:", year, "Program:", show.get('name', 'Unknown'))
    print("Here are your first three clues:")
    index = 1
    while index <= 3:
        print("Clue", index, ":", clues[index - 1])
        index += 1

    attempts = 3
    answer_correct = False

    while attempts > 0:
        guess = input("Enter your answer: ").strip().upper()
        if guess == code_word:
            answer_correct = True
            break
        attempts -= 1
        if attempts > 0:
            print("Incorrect! You have", attempts, "attempts left.")
            if len(clues) > 3:
                print("Additional clue:", clues[3])
        else:
            print("Out of attempts! The correct code word was:", code_word)

    if answer_correct:
        print("Congratulations! You've solved the puzzle and found the treasure!")
    else:
        print("Better luck next time!")

treasury_room("data/TRClues.json")
