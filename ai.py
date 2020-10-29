# Artifitial intelegence part of the game
import random

def players_movies (play_deck, player_order, table_card, play_color, player_choise):
# Players Movies.
    
    m = ['r', 'b', 'g', 'y']

    def player_step_card (player_cards, table_card, play_color):
    # Verifying and choosing play card        
        for temp_card in player_cards: # Find same colour
            if temp_card[0] == play_color:
                return temp_card
        for temp_card in player_cards: # Find same value
            if temp_card[1] == table_card[1]:
                return temp_card
        for temp_card in player_cards: # Find supercard
            if temp_card[0] == '0':
                return temp_card
        return ''

    bet_card = ''

    # Step of the Computer Opponent
    if player_order[0][0] != 'player':
        
        bet_card = player_step_card(player_order[0][1:], table_card, play_color)
        if bet_card[0] != play_color and bet_card[0] != '0':
            play_color = bet_card[0]
            
        if bet_card == '' and len(play_deck) > 0:
                player_order[0].append(play_deck.pop(0))
                bet_card = player_step_card(player_order[0][1:], table_card, play_color)
                if bet_card[0] != play_color and bet_card[0] != '0':
                    play_color = bet_card[0]

        if bet_card != '':
            if bet_card[0] == '0': # Super card
                if bet_card[1] == 'd':
                    player_order.reverse()
                if bet_card[1] == 'p':
                    player_order.append(player_order.pop(0))
                if bet_card[1] == 'f':
                    player_order[1].append(play_deck.pop(0))
                    player_order[1].append(play_deck.pop(0))
                    player_order[1].append(play_deck.pop(0))
                    player_order[1].append(play_deck.pop(0))
                if bet_card[1] == 'c':
                    play_color = m[random.randint(0,3)]
                if bet_card[1] == 'h':
                    k = 100
                    r = 0
                    for i in range(len(player_order)):
                        l = len(player_order[i])
                        if l < k :
                            k = l
                            r = i
                    temp_hand = player_order[0].copy()
                    temp_name1 = player_order[0][0]
                    temp_name2 = player_order[r][0]
                    player_order[0] = player_order[r].copy()
                    player_order[0][0] = temp_name1
                    player_order[r] = temp_hand.copy()
                    player_order[r][0] = temp_name2
            else:
                play_color = bet_card[0]
            
        if bet_card != '':
            player_order[0].pop(player_order[0].index(bet_card))
            play_deck.append(table_card)
            table_card = bet_card

        player_order.append(player_order.pop(0))

    # Step of the Player
    if player_order[0][0] == 'player' :
        
        bet_card = player_step_card(player_order[0][1:], table_card, play_color) # Correction test 1
        if bet_card[0] != play_color and bet_card[0] != '0':
            play_color = bet_card[0]

        if bet_card == '' and len(play_deck) > 0: # Correction test 1
                player_order[0].append(play_deck.pop(0))
                bet_card = player_step_card(player_order[0][1:], table_card, play_color) # Correction test 2
                if bet_card[0] != play_color and bet_card[0] != '0':
                    play_color = bet_card[0]
        
        if bet_card != '':

            bet_card = player_order[0][player_choise + 1]

            if bet_card[0] == '0': # Super card
                if bet_card[1] == 'd':
                    player_order.reverse()
                if bet_card[1] == 'p':
                    player_order.append(player_order.pop(0))
                if bet_card[1] == 'f':
                    player_order[1].append(play_deck.pop(0))
                    player_order[1].append(play_deck.pop(0))
                    player_order[1].append(play_deck.pop(0))
                    player_order[1].append(play_deck.pop(0))
                if bet_card[1] == 'c':
                    play_color = m[random.randint(0,3)]
                if bet_card[1] == 'h':
                    k = 100
                    r = 0
                    for i in range(len(player_order)):
                        l = len(player_order[i])
                        if l < k :
                            k = l
                            r = i
                    temp_hand = player_order[0].copy()
                    temp_name1 = player_order[0][0]
                    temp_name2 = player_order[r][0]
                    player_order[0] = player_order[r].copy()
                    player_order[0][0] = temp_name1
                    player_order[r] = temp_hand.copy()
                    player_order[r][0] = temp_name2
            else:
                play_color = bet_card[0]

        if bet_card != '':
            player_order[0].pop(player_order[0].index(bet_card))
            play_deck.append(table_card)
            table_card = bet_card
        player_order.append(player_order.pop(0))
    
    return play_deck, player_order, table_card, play_color
