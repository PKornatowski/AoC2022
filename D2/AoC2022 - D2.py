# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:36:38 2022

@author: Przemek
"""

input = list(open("input.txt","r"))

points = 0

# A, X Rock = 1
# B, Y Paper = 2
# C, Z Scissors = 3
# Part 2
# X - lose
# Y - draw
# Z - win
translate_moves = {
        "X":"rock",
        "Y":"paper",
        "Z":"scissors",
        "A":"rock",
        "B":"paper",
        "C":"scissors"
        }



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

def move_points(my_move, op_move):
    if translate_moves[my_move] == "rock":
        return 1
    if translate_moves[my_move] == "paper":
        return 2
    if translate_moves[my_move] == "scissors":
        return 3


for item in input:
    op_move=item[0]
    my_move=item[2]
#    print(my_move, "to jest moj ruch")
    points +=  result(my_move, op_move) + move_points(my_move, op_move)
print(points)
        
    