#!/usr/bin/env python

with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

limits = {'red': 12, 'green': 13, 'blue': 14}

for line in lines:
    game_id = line.split(':')
    game_number = int(game_id[0].split(' ')[1])
    games = game_id[1].split(';')
    print(game_number)
    for game in games:
        rounds = game.split(',')
        for round in rounds:
            round_details = round.split(' ')
            round_colour = round_details[1]
            round_value = int(round_details[0])
            if found
        print('---')

