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
        self.hand.append(deck.pop())

    def show_hand(self):
        print(self.hand)

# Playtable class
class Playtable:
    def __init__(self, card):
        self.tablecard = card
    
    def show_playtable(self):
        print(self.tablecard)
    
    def check_play_card(self, card):
        if card[0] == self.tablecard[0] or card[1] == self.tablecard[1]:
            return True
        else:
            return False

if __name__ == '__main__':
    deck = Deck()
    print("New deck created")
    print(f"Deck has {len(deck.play_deck)} cards:")
    deck.show_deck()

    players = []
    for i in range(6):
        players.append(Player(f'Player {i}', deck.play_deck))

    for player in players:
        print(f"{player.name} has {len(player.hand)} cards:")
        player.show_hand()
    
    print("Deck after dealing:")
    print(f"Deck has {len(deck.play_deck)} cards:")
    deck.show_deck()
