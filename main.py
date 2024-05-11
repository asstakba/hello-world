#extrait les mots du fichiers
'''
with open("aliments.txt", "r") as f:
    print(f.read())
'''
#extrait les mots du fichiers en liste
'''
with open("prenoms.txt", "r") as f:
    print(f.readlines())
'''

'''with open("prenoms.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    print(lines)
'''
"""with open("prenoms.txt", "r") as f:
    '''while True:
        s = f.readline()
        if s != "":
            print(s)
        else:
            break
        '''
    while True:
        s = f.readline()
        if s != "":
            print(s.strip())
        else:
            break
"""
'''
with open("prenoms.txt", "r") as f:
    for ligne in f:
        print(ligne)'''

'''with open("prenoms.txt", "r") as f:
    for ligne in f:
        print(ligne.replace('\n', ''))
   
'''
'''with open("aliments.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.replace('\n', ''))
'''

# Fonction pour lire un fichier
# Retourne le contenu du fichier
def read_file(path):
    chaine = ""
    with open(path, 'r', encoding='utf-8') as f:
        chaine = f.read()
    return chaine


# Fonction pour écrire le contenu dans un fichier.
def write_file(path, contenu):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(contenu)

# Fonction qui fait la lecture, la justification, puis l'écriture.
# Aidez-vous de vos fonctions read_file et write_file.
def justifier(path):
    chaine = read_file(path)
    chaine2 = chaine.replace('\n', ' ')
    chaine3 = chaine2.replace('. ', '.\n')
    write_file('phrasesjustier.txt', chaine3)

justifier('phrasesjustier.txt')