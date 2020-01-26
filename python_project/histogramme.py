import matplotlib.pyplot as plt
from functions import *
'''Fichier contenant la méthode de création d'un histogramme à trois entrées'''

def histogram(jour1, jour2, jour3):
    x1 = extract_liste_day(jour1) # on fait appel à la fonction extract_liste_day qui établit une liste de valeurs de NO2 pour chacune des dates
    x2 = extract_liste_day(jour2)
    x3 = extract_liste_day(jour3)
    axes = plt.gca()
    nomabs = ['[0:10]', '[10:20]', '[20:30]','[30:40]', '[40:50]', '[50:60]', '[60:70]', '[70:80]']
    axes.xaxis.set_ticklabels(nomabs, color = 'black', fontsize = 8, style = 'italic', verticalalignment = 'center') # on renomme les abscisses de façon à afficher les intervalles
    bins = [i + 0.5 for i in range(0, 8)]
    h1 = plt.hist([x1, x2, x3], bins=bins, color=['yellow', 'red', 'blue'], edgecolor='green', hatch='/',label=['11/09/2016', '18/09/2017', '25/09/2017'], histtype='bar')
    plt.ylabel('Nombre de Mesures')
    plt.xlabel('Intervalles de Valeurs en microg/m3')
    plt.title("Quantité de NO2 à l'Arc de Triomphe")
    axes.yaxis.grid(True, color = 'orange', linewidth = 0.1, linestyle = 'dashed')
    plt.text(0.4, 10, "Moyenne= "+str(moyenne_day(jour3)), fontsize = 8) # on détermine la moyenne pour le Jour sans voiture 25/09/2016
    plt.text(0.4, 9.5, "Variance= "+ str(variance(jour3)), fontsize =8)  # on détermine la variance
    plt.text(0.4, 9, "Ecart-Type= " + str(ecart_type(jour3)), fontsize = 8) # on détermine l'écart type
    plt.legend()
    plt.show()