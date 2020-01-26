import matplotlib.pyplot as plt
import functions as f
"""Fichier contenant la méthode de création d'une courbe dont l'entrée est la liste de lieux en paramètre"""



# retourne une courbe évolutive de la quantité de NO2 par heure durant la date donnée
def courbe(*lieu, date):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] # heures de la journée
    colors = ['red', 'yellow', 'green', 'blue', 'purple', 'orange', 'black']
    for i in lieu:
        y = f.data_place(i, date, 1, 24) # on extrait les valeurs de NO2 entre 1h et minuit
        plt.plot(x, y, c=colors[lieu.index(i)])

    plt.ylabel('Quantité de NO2 en microg/m3')
    plt.gca().set_xlim(1, 24)
    plt.gca().xaxis.grid(True)
    plt.gca().yaxis.grid(True)
    plt.xlabel('Heures de la Journée')
    plt.title("Evolution de la quantité de NO2 par heure le " + str(date))
    if date == "25/09/2016":
        plt.annotate('Début Journée sans voitures', xy=(11, 40), xytext=(5, 60),arrowprops={'facecolor': 'yellow','width': 1, 'headwidth': 5,'shrink': 0.2}, color='black')
    plt.legend()
    plt.show()