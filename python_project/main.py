import pip
def import_or_install(package):
    try:
        return __import__(package)
    except ImportError:
        pip.main(['install', package])

import_or_install('folium')
import_or_install('googlemaps')
import_or_install('matplotlib')
from menu import *
import os


if __name__ == '__main__':
    
    main_menu()








