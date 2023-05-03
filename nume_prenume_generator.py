import os  # Se importa modulul os, care ofera o interfata cu sistemul de operare.
import random  # Se importa modulul random, care contine functii pentru generarea de numere aleatoare.

nume = ["Popescu", "Ionescu", "Popa", "Dumitru", "Georgescu", "Munteanu", "Marin", "Dinu", "Badea", "Tudor", "Florescu", "Stoica", "Petrescu", "Serban", "Dobrescu", "Chiriac", "Avram", "Nistor", "Craciun", "Nicolae", "Radulescu", "Sandu", "Preda", "Mihai", "Neagu", "Gheorghiu", "Vasilescu", "Radu", "Stanescu", "Toma", "Dumitrache"]
# Se defineste o lista nume care contine nume romanesti.

prenume = ["Alexandra", "Andrei", "Ioana", "Mihai", "Elena", "Vlad", "Ana", "Razvan", "Andreea", "George", "Maria", "Adrian", "Mihaela", "Gabriel", "Alina", "Lucian", "Carmen", "Florin", "Diana", "Marian", "Irina", "Robert", "Simona", "Victor", "Monica", "Cristian", "Raluca", "Alexandru", "Adina", "Bogdan"]
# Se defineste o lista prenume care contine prenume romanesti.

numar_nume = int(input("Cate nume doresti sa generezi? "))
# Se solicita de la utilizator sa introduca numarul de nume aleatoare pe care doreste sa le genereze, care este convertit la integer si atribuit variabilei numar_nume.

nume_fisier = "nume_prenume.txt"
# Se defineste o variabila nume_fisier care contine numele fisierului in care se vor scrie numele si prenumele generate aleatoriu.

cale_fisier = os.path.join(os.path.dirname(__file__), nume_fisier)
# Se construieste calea completa a fisierului nume_prenume.txt, prin concatenarea caii directorului curent al programului si a numelui fisierului.

with open(cale_fisier, "a") as fisier:  # Se deschide fisierul nume_prenume.txt in modul "append"
    for i in range(numar_nume):  # Se itereaza de numar_nume ori
        nume_aleatoriu = random.choice(nume)  # Se alege aleatoriu un nume din lista nume
        prenume_aleatoriu = random.choice(prenume)  # Se alege aleatoriu un prenume din lista prenume
        fisier.write(f"{nume_aleatoriu}\t{prenume_aleatoriu}\n")  # Se scrie numele si prenumele aleatoare in fisierul deschis
print(f"Fisierul {nume_fisier} a fost actualizat cu {numar_nume} nume aleatorii.")
