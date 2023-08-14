# Simplified uno game for the terminal

import random

# Global variables
card_colors = ['r', 'b', 'g', 'y']
card_nominal = ['2', '3', '4', '5', '6', '7', '8', '9', 'd', 'p', 'f', 'c', 'h']

# Card class
class Deck:
    def __init__(self):
        self.play_deck = []
        for i in range(4):
            for j in range(13):
                card = card_colors[i] + card_nominal[j]
                if j > 7:
                    card = '0' + card_nominal[j]
                self.play_deck.append(card)
        random.shuffle(self.play_deck)

    def show_deck(self):
        print(self.play_deck)

# Player class
class Player:
    def __init__(self, name, deck):
        self.name = name
        self.hand = []
        for i in range(6):
            self.draw_card(deck)

    def draw_card(self, deck):
        if len(deck) != 0:
            self.hand.append(deck.pop())
        else:
            self.hand.append('xx')

    def show_hand(self):
        print(self.hand)

# Playtable class
class Playtable:
    def __init__(self, card):
        self.tablecard = card
    
    def show_playtable(self):
        print(self.tablecard)
    
    def check_play_card(self, card):
        if card[0] == '0' or card[0] == self.tablecard[0] or card[1] == self.tablecard[1]:
            return True
        else:
            return False

if __name__ == '__main__':
    # Initialize deck, players and playtable
    deck = Deck()
    players = []
    table = Playtable(deck.play_deck.pop())
    for i in range(6):
        players.append(Player(f'Player {i}', deck.play_deck))
    players[0].name = 'You'

    # Game loop
    no_winner = True
    pass_step = False
    while no_winner:
        print()
        print('~=New round=~')
        print()

        for i in range(len(players)):
            # Show playtable and human player hand
            print(f"Card on table: {table.tablecard}")
            if pass_step:
                print(f"{players[i].name} passes")
                pass_step = False
                continue

            if players[i].name == 'You':
                print(f"Your hand: {players[0].hand}")
                # Get human player input
                while True:
                    card = input('Play a card: ')
                    if card == 'draw':
                        players[i].draw_card(deck.play_deck)
                        break
                    if card in players[i].hand:
                        # Check if card is playable
                        if table.check_play_card(card):
                            table.tablecard = card
                            players[i].hand.remove(card)
                            # Put old one back in deck
                            deck.play_deck.append(table.tablecard)
                            # Wild card processing
                            if card[0] == '0':
                                # Pass card
                                if card[1] == 'p':
                                    pass_step = True
                                # Change color
                                if card[1] == 'c':
                                    while True:
                                        color = input('Choose a color: ')
                                        if color in card_colors:
                                            table.tablecard = color + 'c'
                                            break
                                        else:
                                            print('Invalid color')
                                            continue
                                # Change hand with another player
                                if card[1] == 'h':
                                    while True:
                                        number_of_player = input('Choose player: ')
                                        if int(number_of_player) in range(len(players)):
                                            players[i].hand, players[int(number_of_player)].hand = players[int(number_of_player)].hand, players[i].hand
                                            break
                                        else:
                                            print('Invalid player')
                                            continue
                                # Add next player 4 cards
                                if card[1] == 'f':
                                    for j in range(4):
                                        players[(i + 1) % len(players)].draw_card(deck.play_deck)
                                # Change direction
                                if card[1] == 'd':
                                    players.reverse()
                            break
                        else:
                            print('You cannot play this card')
                            continue
                    else:
                        print('You do not have this card')

                # Check if human player won
                if len(players[0].hand) == 0:
                    print('You won!')
                    no_winner = False
                    break

            else:
                if pass_step:
                    print(f"{players[i].name} passes")
                    pass_step = False
                    continue
                # Get computer player input
                print(f"debug : {players[i].name} has {players[i].hand}")
                for card in players[i].hand:
                    is_card = False
                    # Check if card is playable
                    if table.check_play_card(card):
                        is_card = True
                        print(f"{players[i].name} played {card}")
                        table.tablecard = card
                        players[i].hand.remove(card)
                        # Put old one back in deck
                        deck.play_deck.append(table.tablecard)
                        break

                # Draw card if no card is playable
                if is_card == False:
                    print(f"{players[i].name} draws a card")
                    players[i].draw_card(deck.play_deck)

                # Check if computer player won
                if len(players[i].hand) == 0:
                    print('Computer won!')
                    no_winner = False
                    break
