# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:09:02 2022

@author: Przemek
"""

sample = list(open("input.txt","r"))

#sample = ["1","2","3","6","\n","4","5", "\n","21", "100","\n"]
calories = 0
calorielist = []
for item in sample:
    if item != "\n":
        #print(calories, "przed petla")
        calories = calories + int(item)
        #print(calories, "po petli")
    else:
        #print(calories, "suma pierwszej")
        calorielist.append(calories)
        #print(calorielist, "LISTA Z KALORIAMI")
        calories = 0
#print(index(max(calorielist)))
print(max(calorielist),"elve with most calories")
calorielist.sort(reverse = True)
suma = calorielist[0]+calorielist[1] + calorielist[2]
print(suma, "sum of 3 top elves")


"""
pierwszy=(max(calorielist))
print(pierwszy, "1 wartosc")
print(calorielist.index(pierwszy))
delpierwszy = calorielist.index(pierwszy)
del calorielist[delpierwszy]
drugi=(max(calorielist))
print(drugi, "2 wartosc")
deldrugi = calorielist.index(drugi)
del calorielist[deldrugi]
print(max(calorielist), "3 wartosc")
trzeci = max(calorielist)
suma = pierwszy + drugi + trzeci
print(suma)

#for i in input:
"""