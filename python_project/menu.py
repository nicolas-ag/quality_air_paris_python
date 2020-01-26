from histogramme import *
from courbe import *
from functions import *
from map import *
import sys, os

listcoord = []
for filename in os.listdir('sources/releves'):
    gps_place(os.path.splitext(filename)[0], listcoord)



def main_menu():
    os.system('cls')
    
    print("Analyse de la qualité de l’air à paris durant la JSV 2016 :\n")
    print("Choisir l'élément à afficher:")
    print("1. Afficher l’Histogramme\n")
    print("2. Afficher une courbe\n")
    print("3. Afficher une carte\n")
    print("0. Quitter")
    choice = input(" >>  ")
    exec_menu(choice)
 
    return
 
# Execute menu
def exec_menu(choice):
    os.system('cls')
    ch = choice.lower()
    if ch == '':
        main_menu()
    else:
        try:
            if ch == 'R' or ch == 'r': 
                main_menu()
            if ch == '1': 
                histogram("11/09/2016", "18/09/2016", "25/09/2016")
            if ch =='2': 
                menu1(),
            if ch =='3': 
                menu2(),
            if ch =='4': 
                courbe("Avenue Bonaparte Paris", "Avenue Hausmann", "Avenue Champs-Elysées", "La Défense","Opéra Paris", "Paris 7ème arrondissement","Tour Eiffel", date = "11/09/2016")
            if ch =='5': 
                courbe("Avenue Bonaparte Paris", "Avenue Hausmann", "Avenue Champs-Elysées", "La Défense","Opéra Paris", "Paris 7ème arrondissement","Tour Eiffel", date = "18/09/2016")
            if ch =='6': 
                courbe("Avenue Bonaparte Paris", "Avenue Hausmann", "Avenue Champs-Elysées", "La Défense","Opéra Paris", "Paris 7ème arrondissement","Tour Eiffel", date = "25/09/2016")
            if ch =='7': 
                create_map(listcoord, "11/09/2016")
            if ch =='8': 
                create_map(listcoord, "18/09/2016")
            if ch =='9': 
                create_map(listcoord, "25/09/2016")
            if ch =='0': 
                exit(),
        except KeyError:
            print("Selection invalide, réessayer\n")
            main_menu()
    main_menu()
    return
 
# Menu 1
def menu1():
    print("Choisissez votre date pour afficher la courbe correspondante :\n")
    print("4. Dimanche 11/09/16\n")
    print("5. Dimanche 18/09/16\n")
    print("6. Dimanche 25/09/16 (Journée sans voiture)\n")
    print("R. Retour au menu principal")
    choice = input(" >>  ")
    exec_menu(choice)
    return
 
 
# Menu 2
def menu2():
    print("Choisissez votre date pour afficher la carte correspondante :\n")
    print("7. Dimanche 11/09/16 \n")
    print("8. Dimanche 18/09/16 \n")
    print("9. Dimanche 25/09/16 (Journée sans voiture)\n")
    print("R. Retour au menu principal")
    choice = input(" >>  ")
    exec_menu(choice)
    return
 
# Back to main menu
def back():
    main_menu()
 
# Exit program
def exit():
    sys.exit()
