# Classic Game UNO
# Game classes
import random

# Deck class
class Deck:
    # Deck parameters
    play_deck = []
    color = ['r', 'b', 'g', 'y']
    value = ['2', '3', '4', '5', '6', '7', '8', '9', 'd', 'p', 'f', 'c', 'h']

    # Creating deck
    def __init__(self) -> None:
        for i in range(4):
            for j in range(13):
                card = self.color[i] + self.value[j]
                if j > 7:
                    card = '0' + self.value[j]
                self.play_deck.append(card)
        # Shuffle deck
        random.shuffle(self.play_deck)

    def put_card(self, card):
        self.play_deck.append(card)

    def get_card(self):
        return self.play_deck.pop(0)

curr_deck = Deck()

for card in curr_deck.play_deck:
    print(card)
