# Classic Game UNO

import sys,os
import curses,random
import ai

# Initial section
m = ['r', 'b', 'g', 'y']
z = ['2', '3', '4', '5', '6', '7', '8', '9', 'd', 'p', 'f', 'c', 'h']
player_order = [['player'], ['opponenta'], ['opponentb'], ['opponentc'], ['opponentd'], ['opponente']]
play_deck = []
table_card = ''
play_color = ''
player_choise = 0

# Create and randomize deck of cards
# Innitialize hands of players

# Creating a cards deck
for i in range(4):
  for j in range(13):
    card = m[i] + z[j]
    if j > 7:
      card = '0' + z[j]
    play_deck.append(card)

random.shuffle(play_deck)

# Distribution of cards to players
for i in range(6):
  for j in range(6):
    player_order[i].append(play_deck.pop(0))

# Init step
for i in range(len(play_deck)):
  if play_deck[i][0] != '0' :
    table_card = play_deck.pop(i)
    play_color = table_card[0]
    break

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
step = False

# Clear and refresh the screen for a blank canvas
stdscr.clear()
stdscr.refresh()

# Loop where k is the last character pressed
while (k != ord('q')):
  
  # Step of the Game
  step = False  
  if k == ord('s'):
    step = True

  if step :
    play_deck, player_order, table_card, play_color = \
      ai.players_movies(play_deck, player_order, table_card, play_color, player_choise)
    step = False

  if player_order[0][0] == 'player':
    if k == curses.KEY_RIGHT:
      player_choise = player_choise + 1
    if k == curses.KEY_LEFT:
      player_choise = player_choise - 1
                  
    player_choise = min(len(player_order[0]) - 1, player_choise)
    player_choise = max(player_choise, 0)

  # Draw interface
  stdscr.clear()
    
  stdscr.addstr(0, 0, 'Current player: ' + player_order[0][0])
    
  stdscr.addstr(1, 0, 'Current playcard: ')
  stdscr.addstr(1, 19, table_card, curses.color_pair(5))
  if play_color == 'r':
    stdscr.addstr(1, 19, table_card, curses.color_pair(1))
  if play_color == 'b':
    stdscr.addstr(1, 19, table_card, curses.color_pair(2))
  if play_color == 'g':
    stdscr.addstr(1, 19, table_card, curses.color_pair(3))
  if play_color == 'y':
    stdscr.addstr(1, 19, table_card, curses.color_pair(4))

  j = 2

  for player_to_print in player_order:

    if player_to_print[0] == 'player':
      stdscr.addstr(j, 0, 'Player hand: ', curses.A_BOLD)
      for i in range(len(player_to_print) - 1):
        if i == player_choise :
          stdscr.addstr(j, 14 + 3*i, player_to_print[i+1], curses.A_REVERSE)
          stdscr.addstr(j, 38, str(player_choise), curses.A_REVERSE)
          continue
        if player_to_print[i+1][0] == 'r':
          stdscr.addstr(j, 14 + 3*i, player_to_print[i+1], curses.color_pair(1))
        if player_to_print[i+1][0] == 'b':
          stdscr.addstr(j, 14 + 3*i, player_to_print[i+1], curses.color_pair(2))
        if player_to_print[i+1][0] == 'g':
          stdscr.addstr(j, 14 + 3*i, player_to_print[i+1], curses.color_pair(3))
        if player_to_print[i+1][0] == 'y':
          stdscr.addstr(j, 14 + 3*i, player_to_print[i+1], curses.color_pair(4))
        if player_to_print[i+1][0] == '0':
          stdscr.addstr(j, 14 + 3*i, player_to_print[i+1], curses.color_pair(5))
    else:
      stdscr.addstr(j, 0, player_to_print[0] + ': ' + str(len(player_to_print[1:])))

    j = j + 1
    
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
