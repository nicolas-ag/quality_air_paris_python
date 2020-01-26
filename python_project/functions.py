import csv
from collections import Counter
from math import sqrt
import googlemaps
"""Fichier contenant toutes les méthodes pour l'extractions de données 
   Et les méthodes de calculs de statistiques pour l'histogramme """


# méthode retournant une liste de nombre de valeurs de NO2 contenus dans chaque intervalles
def extract_liste_day(jour):
    dictintervalles = dict(
        [('0:10', 'no'), ('10:20', 'no'), ('20:30', 'no'), ('30:40', 'no'), ('40:50', 'no'), ('50:60', 'no'),
         ('60:70', 'no'), ('70:80', 'no')])

    listNO2 = champs_elysees_no2(jour)
    nb0_10 = 0
    nb10_20 = 0
    nb20_30 = 0
    nb30_40 = 0
    nb40_50 = 0
    nb50_60 = 0
    nb60_70 = 0
    nb70_80 = 0
    width = 1.0
    listStats = []

    for i in listNO2:
        if i > 0 and i <= 10:
            listStats.append(1)

        if i > 10 and i <= 20:
            listStats.append(2)

        if i > 20 and i <= 30:
            listStats.append(3)

        if i > 30 and i <= 40:
            listStats.append(4)

        if i > 40 and i <= 50:
            listStats.append(5)

        if i > 50 and i <= 60:
            listStats.append(6)

        if i > 60 and i <= 70:
            listStats.append(7)

        if i > 70 and i <= 80:
            listStats.append(8)

    return (sorted(listStats))


# méthode qui extrait toutes les données NO2 prélevées sur les champs elysées à une date donnée
def champs_elysees_no2(jour):
    with open('sources/qualiteair-champs_elysees.csv', mode='r', encoding='utf8') as f:
        r = csv.reader(f)
        l = list(r)
        listNO2Day = []
        length = len(l)

        for i in range(2, length): # on parcourt la liste à partir de 2 car les deux première lignes sont les noms de chaque colonnes et les unités
            ligne = l[i]
            case = ligne[0]
            ani = case.split(";")

            if ani[0] == jour:
                NO2 = int(ani[3])
                listNO2Day.append(NO2)

        return (listNO2Day)


# retourne la moyenne d'une liste
def moyenne_liste(Liste):
    somme = 0
    N = len(Liste)
    for i in Liste:
        if i == 'n/d':
            continue
        else:
            somme = somme + i
    moyenne = somme / N
    return moyenne


# retourne la moyenne des valeurs mesurées à un endroit entre une heure de départ et de fin
def moyenne_place_day(place, day, heure_deb, heure_fin):
    return moyenne_liste(data_place(place, day, heure_deb, heure_fin)) # fait appel à deux fonctions


# retourne la moyenne des valeurs de NO2 selon la journée
def moyenne_day(jour):
    somme = 0
    listNO2 = extract_liste_day(jour) # fait appel à la fonction qui extrait une liste de valeurs de NO2

    nbvalues = len(listNO2)
    for i in listNO2:
        somme = somme + i

    Moyenne = somme / nbvalues
    return Moyenne


 # retourne la variance selon la journée
def variance(jour):
    somme = 0
    SommeVariance = 0
    totale = 0
    Variance = 0
    listVariance = []
    listNO2 = extract_liste_day(jour)

    cpt = Counter(listNO2)
    couple = [(cpt[i], i) for i in cpt] # retourne chaque couple avec la valeur "x" et son sa récurrence "n" dans la listNO2
    listVariance.append(couple)

    N = len(listNO2)
    size = len(listVariance)

    y = listVariance[0]
    size = len(y)
    for i in range(0, size):
        z = y[i]
        n1 = z[0] #récurrence
        x1 = z[1] * z[1] # valeur
        som = n1 * x1
        SommeVariance = SommeVariance + som
    moycarre = moyenne_day(jour) ** 2

    Variance = SommeVariance / N - moycarre
    return Variance


# retourne la racine carré de la variance
def ecart_type(jour):
    var = variance(jour)
    ecartype = sqrt(var)
    return ecartype


#retourne une liste de valeur de NO2 à ue date et une place préçise entre deux heures données
def data_place(lieu, date, heure_deb, heure_fin):
    with open('sources/releves/' + lieu + '.csv', mode='r', encoding='utf8') as f: #on va chercher le fichier
        r = csv.reader(f)
        l = list(r)
        length = len(l)
        listData = []
        first_line = l[0]
        columns = first_line[0]
        list_of_columns = columns.split(";")
        index_NO2 = list_of_columns.index('NO2') #parmi les intitulés de colonnes on cherche l'indice de 'NO2'
        for i in range(2, length): #on commence à partir de la 2 car les deux premières lignes sont des intitulés des unités
            ligne = l[i]
            case = ligne[0]
            value_list = case.split(";")
            if value_list[0] == date and int(value_list[1])>=heure_deb and int(value_list[1])<=heure_fin:
                if value_list[index_NO2] == 'n/d': # dans le cas où il n'y aurait pas de valeur
                    continue
                else:
                    NO2 = int(value_list[index_NO2])
                    listData.append(NO2)

    return (listData)


 # renvoie grâce à une requête sur l'api google les coordonnées géographiques d'un lieu et le rajoute à la liste listcoord
def gps_place(lieu, listcoord):
    gmaps = googlemaps.Client(key='AIzaSyCPTapMMa8wwsz7yUQZH0WWIA9nd_kIKeY') # clé permettant de faire les requêtes
    geocode_result = gmaps.geocode(lieu)
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]

    point = dict([('nom', lieu), ('lat', lat), ('long', lon)])
    listcoord.append(point) # on ajoute le dictionnaire a listcoord
