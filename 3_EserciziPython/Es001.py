#Scrivere un programma che riempia una lista arbitraria chiedendo i valori degli elementi all'utente
ancora = True
dim = input("quanti numeri vuoi inserire?")
lista = []

for i in range(int (dim)):
    x= input("Inserisci un numero")
    lista.append(x)

print(lista)

