import random

def introduction():
    print("Welcome to the Treasure Hunt Game!")
    print("In this game, you will complete challenges to earn keys.")
    print("The objective is to collect three keys to unlock the treasure room.")
    print("Good luck on your adventure!")


def compose_equipe():
    equipe = []
    nombre_joueurs = 0
    while nombre_joueurs <= 0 or nombre_joueurs > 3:
        nombre_joueurs = int(input("How many players would you like to include in the team? "))
        if nombre_joueurs <= 0 or nombre_joueurs > 3:
            print("Error: You can have a maximum of 3 players. Please enter a valid number.")

    for i in range(1, nombre_joueurs + 1):
        name = input("Enter the name of player " + str(i) + ": ")
        profession = input("Enter the profession of player " + name + ": ")
        is_leader_input = input("Is " + name + " the team leader? (yes/no): ").lower()
        is_leader = is_leader_input == "yes"
        player = {"name": name, "profession": profession, "is_leader": is_leader, "keys_wons": 0}
        equipe.append(player)

    leader_found = False
    for player in equipe:
        if player["is_leader"]:
            leader_found = True
    if not leader_found:
        equipe[0]["is_leader"] = True

    return equipe


def challenges_menu():
    print("Please choose a challenge from the following options:")
    print("1. Mathematics challenge")
    print("2. Logic challenge")
    print("3. Chance challenge")
    print("4. Père Fourras' riddle")
    choice = int(input("Enter the number corresponding to your chosen challenge: "))
    while choice < 1 or choice > 4:
        print("Error: Invalid choice. Please choose a number between 1 and 4.")
        choice = int(input("Enter the number corresponding to your chosen challenge: "))
    return choice


def choose_player(team):
    print("Please choose a player to take on the challenge:")
    for index, player in enumerate(team, start=1):
        role = "Leader" if player["is_leader"] else "Member"
        print(f"{index}. {player['name']} ({player['profession']}) - {role}")
    player_number = int(input("Enter the player's number: "))
    while player_number < 1 or player_number > len(team):
        print("Error: Invalid choice. Please enter a number corresponding to a player in the team.")
        player_number = int(input("Enter the player's number: "))
    return team[player_number - 1]


import os
def record_history(challenge_name: str, player: dict, result: str, keys_won: int) -> None:
    if not os.path.exists('output'):
        os.makedirs('output')
    with open('output/history.txt', 'a') as file:
        file.write(f"{challenge_name} - {player['name']} - {result} - {keys_won} keys\n")


introduction()

team = compose_equipe()

challenge_choice = challenges_menu()

selected_player = choose_player(team)

result = "Success"
keys_won = 1

record_history("Mathematics challenge", selected_player, result, keys_won)











