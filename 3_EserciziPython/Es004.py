#esercizio che genera numeri casuali
""" 
le librerie hanno nomi lunghi quindi posso usare deglia aia(sinonimi) tipo import random as rnd
"""
#importo le librerie con import
import random

nameList = ['Mario Rossi', 'John Doe', 'Tizio Caio']

#richiamo la funzione che mi serve e che è nella libreria -> nomino la libreria e con il . definisco la funzione
#restituisce numeri interi dai numeri

#print(random.randint(0,len(nameList)))

#random.randint(0,len(nameList)-1)   #restituisce fino alla lunghezza -1

for num, student in enumerate(nameList):    #funzione enumerate ->ritorna sia l'elemento che la posizione
    print(f"{num} - {student}")     #cicla sia sull'elemento che sulla posizione

print(f"Viene interrogato: {nameList[random.randint(0,len(nameList)-1)]}")
