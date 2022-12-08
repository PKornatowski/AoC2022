# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 22:09:46 2022

@author: Przemek
"""

input = list(open("sample.txt","r"))
formatted_input = []
new_formatted_input = []
common_summed = []
value = 0
test = []
#part 1
#upper_cases = range[A,Z]
"""
for rucksack in input:
    left_side = rucksack[:len(rucksack)//2]
    right_side = rucksack[len(rucksack)//2:]
    new_input_line = (left_side,right_side)
    formatted_input.append(new_input_line)

for left_side, right_side in formatted_input:
    common_item = tuple(set(left_side) & set(right_side))[0]
    common_summed.append(common_item)
    if common_item.islower():
        value += ord(common_item)-96
    else:
        value += ord(common_item) - 38
    
    
#    print(ord(common_item))
"""
#part 2


for rucksack in input:
    new_input_line = (rucksack)
    formatted_input.append(new_input_line)
    
max_index = len(formatted_input) 
  
for i in range(1, max_index, 3):
    divided_input = (formatted_input[i-1], formatted_input[i], formatted_input[i+1])
    new_formatted_input.append(divided_input)
    
new_max_index = len(new_formatted_input)

for first_elv, second_elv, third_elv in new_formatted_input:
#    print(first_elv)
 #   print(second_elv)
#    print(third_elv)
    common = tuple(set(first_elv) & set(second_elv) & set(third_elv))[0]
    print(common)
    common_summed.append(common)
#    common_item = tuple(set(first_elv) & set(second_elv) & set(third_elv))[0]
    if common.islower():
        value += ord(common)-96
        print(ord(common)-96,"mała litera")
    else:
        value += ord(common) - 38
        print(ord(common) - 38,"duża litera")


#print(ord("H")-96)

"""
for i in range(1,27):
    value = i
    print(value)
    
for rucksack in input:
    left_side = (rucksack[:len(rucksack)//2])
    right_side = (rucksack[len(rucksack)//2:])
    formatted_input.append([(left_side), (right_side)])


for pozycja in formatted_input:
    common_item = list(set(pozycja[0]) & set(pozycja[1]))
    common_summed.append(common_item)
for element in common_summed:
    print((ord(element[0])) -96)
    
test=ord("a")
test2=test-96
    
    
    # new_line = ((rucksack[:len(rucksack)//2]), (rucksack[len(rucksack)//2:]))
    
"""