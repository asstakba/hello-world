'''with open('fichiersCSV.csv ','r') as f:
    print(f.read())'''
'''
import csv

# Ouverture du fichier CSV en mode lecture
with open("exemple.csv", newline='') as fichier_csv:
    # Création d'un objet lecteur CSV
    lecteur_csv = csv.reader(fichier_csv)

    # Lecture des lignes une à une
    for ligne in lecteur_csv:
        print(ligne)'''
'''
import csv
import codecs
# Ouverture du fichier CSV en mode lecture
with codecs.open("exemple.csv", encoding="utf-8") as fichier_csv:
    # Création d'un objet lecteur CSV
    lecteur_csv = csv.reader(fichier_csv)

    # Lecture des lignes une à une
    for ligne in lecteur_csv:
        print(ligne)'''

'''# Importation de la librairie
import tkinter as tk
# Création de l'élément racine
root = tk.Tk()
# Affiche de la fenêtre
root.mainloop()

print("Ce code sera exécuté à la fermeture de la fenêtre Tkinter")'''
'''
import tkinter as tk
root = tk.Tk()
root.title("Mon premier programme")
root.geometry("300x100")
root.mainloop();'''

import csv
# ouverture en lecture
fp = open('people.csv', 'r')
reader = csv.DictReader(fp, delimiter=‘;')
# afficher
for ligne in reader:
    print(ligne)
    for cle, valeur in ligne.items():
        print(cle, valeur)
# fermeture
fp.close()

