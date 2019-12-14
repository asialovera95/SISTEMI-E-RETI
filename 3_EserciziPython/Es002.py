#chieda all'utente una lista di parole poi un numero (lunghezza) produce una lista di parole con solo le parole più lunghe di quel numero inserito

ancora = True
nParole = input("quante parole vuoi?")
dim = input("quanti vuoi che sia la lunghezza di una parola?")
lista = []

for i in range(int (nParole)):
    x= input("Inserisci una parola")
    if(len(x)> dim):
        lista.append(x)

print(lista)
