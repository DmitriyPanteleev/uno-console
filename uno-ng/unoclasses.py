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
        if len(self.play_deck) == 0 :
            return "empty"
        return self.play_deck.pop(0)

# Player class
class Player:
    # Player parameters
    name = ""
    hand_cards = []
    credit = 0

    # Creating playres
    def __init__(self, name) -> None:
        self.name = name
        self.hand_cards = []

    def get_card(self, card):
        self.hand_cards.append(card)

    def do_step(self, card):
        for i_card in self.hand_cards:
            if i_card[0] == card[0]:
                self.hand_cards.remove(i_card)
                return i_card
        for i_card in self.hand_cards:
            if i_card[1] == card[1]:
                self.hand_cards.remove(i_card)
                return i_card
        return 'get_card_from_deck'

if __name__ == '__main__':

    curr_deck = Deck()

    gamer = Player('gamer')
    player1 = Player('player1')
    player2 = Player('player2')
    player3 = Player('player3')
    player4 = Player('player4')
    player5 = Player('player5')
    players = [gamer, player1, player2, player3, player4, player5]

    for player in players:
        for i in range(1):
            card = curr_deck.get_card()
            if card != "empty":
                player.get_card(card)
            else:
                print("The deck is empty")

    print(curr_deck.play_deck)    
    for player in players:
        print(player.name)
        print(player.hand_cards)
