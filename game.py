from random import randint
import os


game_running = True
round_list = []

# Testing Git Push
# Michael was here

def game_over(winner, loser):

    print(f"{winner} was victorious in defeating {loser}!")


while game_running:

    # clear the terminal screen when game.py is ran, doesn't seem to work for the integrated terminal in VS Code
    os.system('cls' if os.name == 'nt' else 'clear')

    rounds_counter = 0
    new_round = True
    player = {'name': 'Michael', 'attack': 12,
              'heal': 16, 'health': 100}
    monster = {'name': 'Monster', 'attack_min': 10, 'attack_max': 20,
               'heal': 16, 'health': 100}

    def monster_attack(attack_min, attack_max):
        """ function to return a random attack damage between minimum and maximum damage for a monster """
        return randint(monster['attack_min'], monster['attack_max'])

    print('*********' * 6)
    print('What brave soul is this?')
    player['name'] = input()
    print(f"{player['name']}, may God have mercy on you! \n")
    print(
        f"You have {player['health']} HP and the {monster['name']} has {monster['health']} HP. Go forth!!")
    print('*********' * 6)

    while new_round:

        rounds_counter += 1
        player_won = False
        monster_won = False

        print('Please select an action: \n')

        print('1) Attack')
        print('2) Heal')
        print('3) Exit')
        print("4) Player's Stats")

        player_choice = input()

        if player_choice == '1':
            monster['health'] -= player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] -= monster_attack(
                    monster['attack_min'], monster['attack_max'])
                if player['health'] <= 0:
                    monster_won = True
            print('')

        elif player_choice == '2':
            print('')
            print(
                f"{player['name']} uses healing potion and gained {player['heal']} HP")
            player['health'] += player['heal']
            print(f"You're back to {player['health']} HP now \n")

            # Monster turn to attack
            random_damage = monster_attack(
                monster['attack_min'], monster['attack_max'])
            print(
                f"{monster['name']} attack you for {random_damage} damage")
            player['health'] -= random_damage

            if player['health'] <= 0:
                monster_won = True

        elif player_choice == '3':
            game_running = False
            new_round = False
            print('Thanks for playing. Good bye')

        elif player_choice == '4':
            for items in round_list:
                print(items)
        else:
            print('That is not a valid choice! Please choose again.')

        if player_won == False and monster_won == False:
            print(f"You have {player['health']} HP left")
            print(f"The {monster['name']} has {monster['health']} HP left \n")

        elif player_won:
            print(f"Congrats {player['name']}. You've won!")
            game_over(player['name'], monster['name'])
            round_results = {
                'name': player['name'], 'health': player['health'], 'rounds': rounds_counter}
            round_list.append(round_results)
            new_round = False

        elif monster_won:
            print('You are DEAD! RIP \n')
            game_over(monster['name'], player['name'])
            round_results = {
                'name': player['name'], 'health': player['health'], 'rounds': rounds_counter}
            round_list.append(round_results)
            new_round = False
