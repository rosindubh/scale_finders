# taken from magpi issue 54 page 71
# the game of bunco recreated using procedural programming
# phil welsby 1 february 2017

import random

player1_dice = []
player2_dice = []

for i in range(3):
    player1_dice.append(random.randint(1,6))
    player2_dice.append(random.randint(1,6))

print('Player 1 rolled' + str(player1_dice))
print('Player 2 rolled' + str(player2_dice))

if sum(player1_dice) == sum(player2_dice):
    print('Draw')
elif sum(player1_dice) > sum(player2_dice):
    print('Player 1 wins')
else:
    print('Player 2 wins')
