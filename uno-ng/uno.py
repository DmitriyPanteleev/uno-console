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

if __name__ == '__main__':
    deck = Deck()
    print(f"Deck has {len(deck.play_deck)} cards:")
    deck.show_deck()
