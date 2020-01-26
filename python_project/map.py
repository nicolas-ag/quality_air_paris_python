import functions as f
import webbrowser
import folium
import os
"""Fichier contenant la méthode de création des points en utilisant la librairie folium"""


webbrowser.register('chrome', None, webbrowser.GenericBrowser('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'))
a=webbrowser.get('chrome')

#crée tous les points dans la liste de dicitonnaires listcoord
def create_map(bigDict, date):
    map_osm = folium.Map(location=[48.8649451, 2.3207429], zoom_start=12.5)
    folium.TileLayer('cartodbpositron').add_to(map_osm)


    for lieu in bigDict: #on parcours tous les points de la liste de dictonnaire
        color = 'blue'
        moyenne = f.moyenne_place_day(lieu.get('nom'), date, 11, 17) # on calcule la moyenne de chaque point pour déterminer son code couleur
        color = "blue"
        if moyenne < 25:
            color = "green"
        elif moyenne > 25 and moyenne < 40:
            color = "yellow"
        elif moyenne > 40 and moyenne < 65:
            color = "orange"
        else:
            color = "red"
        folium.CircleMarker([lieu.get('lat'), lieu.get('long')], radius=25, popup= lieu.get('nom')+' [ indice NO2 : '+str(moyenne.__round__ (2)) + ' ]  le '+ str(date),color=color, fill = True, fill_color = color).add_to(map_osm)

    map_osm.save('./map_osm.html')
    a.open(os.getcwd() + "/map_osm.html")
    map_osm