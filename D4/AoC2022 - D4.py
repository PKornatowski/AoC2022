# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 18:00:26 2022

@author: Przemek
"""



input = list(open("input.txt","r"))
overlaps = 0


def range_checks(frs,fre,srs,sre):
    first_range = range(frs,fre+1)
    second_range = range(srs, sre+1)
    first_range_set = set(first_range)
    second_range_set = set(second_range)
    if first_range_set.issubset(second_range_set):
        return 1
    if second_range_set.issubset(first_range_set):
        return 1
    else:
        return 0
def parse_text(line):
    ranges = line.split(",")
    first_range = ranges[0].split("-")
    first_range_start = first_range[0]
    first_range_end = first_range[1]
    second_range = ranges[1].split("-")
    second_range_start = second_range[0]
    second_range_end = second_range[1]
    return int(first_range_start), int(first_range_end), int(second_range_start), int(second_range_end)

def any_overlap(frs, fre, srs, sre):
    first_range = range(frs, fre+1)
    second_range = range(srs, sre+1)
    if srs in first_range or sre in first_range:
        return 1
    elif fre in second_range or frs in second_range:
        return 1
    else:
        return 0
    

for line in input:
     frs, fre, srs, sre = parse_text(line)
#Part 1     overlaps += range_checks(frs, fre, srs, sre)
     overlaps += any_overlap(frs, fre, srs, sre)
