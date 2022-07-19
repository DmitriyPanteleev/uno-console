# Classic Game UNO

import sys,os
import curses,random
import unoclasses

# Create and randomize deck of cards
# Innitialize hands of players

m = ['r', 'b', 'g', 'y']
z = ['2', '3', '4', '5', '6', '7', '8', '9', 'd', 'p', 'f', 'c', 'h']
player_order = ['player', 'opponenta', 'opponentb']
play_deck = []
table_deck = []
play_card = '  '
play_color = 'r'
bet_card = ''
player_hand = []
opponenta_hand = []
opponentb_hand = []
first_step = True

for i in range(4):
    for j in range(13):
        card = m[i] + z[j]
        if j > 7:
            card = '0' + z[j]
        play_deck.append(card)
random.shuffle(play_deck)

for i in range(6):
    player_hand.append(play_deck.pop(0))
    opponenta_hand.append(play_deck.pop(0))
    opponentb_hand.append(play_deck.pop(0))

# Define functions

def opponent_step(opponent_hand):
    global play_color
    global play_card
    for temp_card in opponent_hand:
        if temp_card[0] == play_color:
            play_color = temp_card[0]
            return temp_card
    for temp_card in opponent_hand:
        if temp_card[1] == play_card[1]:
            play_color = temp_card[0]
            return temp_card
    for temp_card in opponent_hand:
        if temp_card[0] == '0':
            return temp_card
    return ''

# Initialize/create windows
# create a window object that represents the terminal window
stdscr = curses.initscr()
# Don't print what I type on the terminal
curses.noecho()
# React to every key press, not just when pressing "enter"
curses.cbreak()
# Hide cursor
curses.curs_set(0)
# Enable easy key codes (will come back to this)
stdscr.keypad(True)
stdscr.border(1)
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

# Main Program!!!
height, width = stdscr.getmaxyx()
k = 0
player_choise = 0
play_round = True
step = False

# Clear and refresh the screen for a blank canvas
stdscr.clear()
stdscr.refresh()

# Loop where k is the last character pressed
while (k != ord('q')):
    
    if k == ord('s'):
        step = True

    if step : # Step of the Game et AI

        if player_order[0] == 'player' :
            if opponent_step(player_hand) == '':
                if len(play_deck) > 0:
                    player_hand.append(play_deck.pop(0))
            if opponent_step(player_hand) != '':
                bet_card = player_hand.pop(player_choise)
                player_choise = 0
                if bet_card[0] == '0': # Super card
                    if bet_card[1] == 'd':
                        player_order.reverse()
                    if bet_card[1] == 'p':
                        player_order.append(player_order.pop(0))
                    if bet_card[1] == 'f':
                        if player_order[1] == 'opponenta':
                            opponenta_hand.append(play_deck.pop(0))
                            opponenta_hand.append(play_deck.pop(0))
                            opponenta_hand.append(play_deck.pop(0))
                            opponenta_hand.append(play_deck.pop(0))
                        if player_order[1] == 'opponentb':
                            opponentb_hand.append(play_deck.pop(0))
                            opponentb_hand.append(play_deck.pop(0))
                            opponentb_hand.append(play_deck.pop(0))
                            opponentb_hand.append(play_deck.pop(0))
                    if bet_card[1] == 'c':
                        play_color = m[random.randint(0,3)]
                    if bet_card[1] == 'h':
                        temp_hand = player_hand.copy()
                        if len(opponenta_hand) < len(opponentb_hand):
                            player_hand = opponenta_hand.copy()
                            opponenta_hand = temp_hand.copy()
                        else:
                            player_hand = opponentb_hand.copy()
                            opponentb_hand = temp_hand.copy()
            
        if player_order[0] == 'opponenta' :
            bet_card = opponent_step(opponenta_hand)
            if bet_card == '':
                if len(play_deck) > 0:
                    opponenta_hand.append(play_deck.pop(0))
                    bet_card = opponent_step(opponenta_hand)
            if bet_card[0] == '0': # Super card
                if bet_card[1] == 'd':
                    player_order.reverse()
                if bet_card[1] == 'p':
                    player_order.append(player_order.pop(0))
                if bet_card[1] == 'f':
                    if player_order[1] == 'player':
                        player_hand.append(play_deck.pop(0))
                        player_hand.append(play_deck.pop(0))
                        player_hand.append(play_deck.pop(0))
                        player_hand.append(play_deck.pop(0))
                    if player_order[1] == 'opponentb':
                        opponentb_hand.append(play_deck.pop(0))
                        opponentb_hand.append(play_deck.pop(0))
                        opponentb_hand.append(play_deck.pop(0))
                        opponentb_hand.append(play_deck.pop(0))
                if bet_card[1] == 'c':
                    play_color = m[random.randint(0,3)]
                if bet_card[1] == 'h':
                    temp_hand = opponenta_hand.copy()
                    if random.randint(0,9) < 5 :
                        opponenta_hand = opponentb_hand.copy()
                        opponentb_hand = temp_hand.copy()
                    else:
                        opponenta_hand = player_hand.copy()
                        player_hand = temp_hand.copy()
            if bet_card != '':
                opponenta_hand.pop(opponenta_hand.index(bet_card))

        if player_order[0] == 'opponentb' :
            bet_card = opponent_step(opponentb_hand)
            if bet_card == '':
                if len(play_deck) > 0:
                    opponentb_hand.append(play_deck.pop(0))
                    bet_card = opponent_step(opponentb_hand)
            if bet_card[0] == '0': # Super card
                if bet_card[1] == 'd':
                    player_order.reverse()
                if bet_card[1] == 'p':
                    player_order.append(player_order.pop(0))
                if bet_card[1] == 'f':
                    if player_order[1] == 'player':
                        player_hand.append(play_deck.pop(0))
                        player_hand.append(play_deck.pop(0))
                        player_hand.append(play_deck.pop(0))
                        player_hand.append(play_deck.pop(0))
                    if player_order[1] == 'opponentb':
                        opponenta_hand.append(play_deck.pop(0))
                        opponenta_hand.append(play_deck.pop(0))
                        opponenta_hand.append(play_deck.pop(0))
                        opponenta_hand.append(play_deck.pop(0))
                if bet_card[1] == 'c':
                    play_color = m[random.randint(0,3)]
                if bet_card[1] == 'h':
                    temp_hand = opponentb_hand.copy()
                    if random.randint(0,9) < 5 :
                        opponentb_hand = opponenta_hand.copy()
                        opponenta_hand = temp_hand.copy()
                    else:
                        opponenta_hand = player_hand.copy()
                        player_hand = temp_hand.copy()
            if bet_card != '':
                opponentb_hand.pop(opponentb_hand.index(bet_card))        
        
        if bet_card != '':
            table_deck.append(play_card)
            play_card = bet_card
            player_order.append(player_order.pop(0))

        step = False

    if player_order[0] == 'player':
        if k == curses.KEY_RIGHT:
            player_choise = player_choise + 1       
        if k == curses.KEY_LEFT:
            player_choise = player_choise - 1
                
    player_choise = min(len(player_hand) - 1, player_choise)
    player_choise = max(player_choise, 0)

    # Draw interface
    stdscr.clear()
    
    stdscr.addstr(0, 0, 'Current player: ' + player_order[0])
    
    stdscr.addstr(1, 0, 'Current playcard: ')
    stdscr.addstr(1, 19, play_card, curses.color_pair(5))
    if play_color == 'r':
        stdscr.addstr(1, 19, play_card, curses.color_pair(1))
    if play_color == 'b':
        stdscr.addstr(1, 19, play_card, curses.color_pair(2))
    if play_color == 'g':
        stdscr.addstr(1, 19, play_card, curses.color_pair(3))
    if play_color == 'y':
        stdscr.addstr(1, 19, play_card, curses.color_pair(4))

    stdscr.addstr(2, 0, 'Player hand: ')
    if player_order[0] == 'player':
        stdscr.addstr(2, 0, 'Player hand: ', curses.A_BOLD)
    for i in range(len(player_hand)):
        if i == player_choise :
            stdscr.addstr(3, 3*i, player_hand[i], curses.A_REVERSE)
            continue
        if player_hand[i][0] == 'r':
            stdscr.addstr(3, 3*i, player_hand[i], curses.color_pair(1))
        if player_hand[i][0] == 'b':
            stdscr.addstr(3, 3*i, player_hand[i], curses.color_pair(2))
        if player_hand[i][0] == 'g':
            stdscr.addstr(3, 3*i, player_hand[i], curses.color_pair(3))
        if player_hand[i][0] == 'y':
            stdscr.addstr(3, 3*i, player_hand[i], curses.color_pair(4))
        if player_hand[i][0] == '0':
            stdscr.addstr(3, 3*i, player_hand[i], curses.color_pair(5))
    
    stdscr.addstr(4, 0, 'OpponentA hand: ' + str(len(opponenta_hand)))
    if player_order[0] == 'opponenta':
            stdscr.addstr(4, 0, 'OpponentA hand: ' + str(len(opponenta_hand)), curses.A_BOLD)

    stdscr.addstr(5, 0, 'OpponentB hand: ' + str(len(opponentb_hand)))
    if player_order[0] == 'opponentb':
            stdscr.addstr(5, 0, 'OpponentB hand: ' + str(len(opponentb_hand)), curses.A_BOLD)
    
    # Refresh the screen
    stdscr.refresh()

    # Wait for next input
    k = stdscr.getch()

# Destroy windows
# reverse everything that you changed about the terminal
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
# restore the terminal to its original state
curses.endwin()
