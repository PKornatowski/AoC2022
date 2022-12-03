# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:36:38 2022

@author: Przemek
"""



# A, X Rock = 1
# B, Y Paper = 2
# C, Z Scissors = 3
# Part 2
# X - lose
# Y - draw
# Z - win
input = list(open("input.txt","r"))
points = 0
translate_moves = {
        "X":"lose",
        "Y":"draw",
        "Z":"win",
        "A":"rock",
        "B":"paper",
        "C":"scissors"
        }
moves = ["scissors", "rock", "paper"]

def what_to_play(my_outcome, op_move):
    if translate_moves[my_outcome] == "win":
        index_number = (moves.index(translate_moves[op_move]) +1) %3
        return moves[index_number]
    if translate_moves[my_outcome] == "draw":
        index_number = moves.index(translate_moves[op_move])
        return moves[index_number]
    if translate_moves[my_outcome] == "lose":
        index_number = (moves.index(translate_moves[op_move]) -1) %3
        return moves[index_number]


def move_points(my_move):
    if my_move == "rock":
        return 1
    if my_move == "paper":
        return 2
    if my_move == "scissors":
        return 3

def round_points(my_outcome):
    if translate_moves[my_outcome] == "win":
        return 6
    if translate_moves[my_outcome] == "draw":
        return 3
    if translate_moves[my_outcome] == "lose":
        return 0

for item in input:
    op_move=item[0]
    my_outcome=item[2]
    my_move = what_to_play(my_outcome, op_move)
    points += move_points(my_move) + round_points(my_outcome)
print(points)


"""
def result(my_move, op_move):
    if translate_moves[my_move] == "rock" and translate_moves[op_move] == "scissors":
#        print("win")
        return 6
    if translate_moves[my_move] == "paper" and translate_moves[op_move] == "rock":
#        print("win")
        return 6
    if translate_moves[my_move] == "scissors" and translate_moves[op_move] == "paper":
#        print("win")
        return 6
    if translate_moves[my_move] == translate_moves[op_move]:
#        print("draw")
        return 3
#    print("lose")
    return 0
"""
        
    