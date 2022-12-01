# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:09:02 2022

@author: Przemek
"""

sample = list(open("input.txt","r"))

#sample = ["1","2","3","6","\n","4","5", "\n","21", "100","\n"]
kalorie = 0
listakalori = []
for item in sample:
    if item != "\n":
        #print(kalorie, "przed petla")
        kalorie = kalorie + int(item)
        #print(kalorie, "po petli")
    else:
        #print(kalorie, "suma pierwszej")
        listakalori.append(kalorie)
        #print(listakalori, "LISTA Z KALORIAMI")
        kalorie = 0
#print(index(max(listakalori)))
print(max(listakalori),"elve with most calories")
listakalori.sort(reverse = True)
suma = listakalori[0]+listakalori[1] + listakalori[2]
print(suma, "sum of 3 top elves")


"""
pierwszy=(max(listakalori))
print(pierwszy, "1 wartosc")
print(listakalori.index(pierwszy))
delpierwszy = listakalori.index(pierwszy)
del listakalori[delpierwszy]
drugi=(max(listakalori))
print(drugi, "2 wartosc")
deldrugi = listakalori.index(drugi)
del listakalori[deldrugi]
print(max(listakalori), "3 wartosc")
trzeci = max(listakalori)
suma = pierwszy + drugi + trzeci
print(suma)

#for i in input:
"""