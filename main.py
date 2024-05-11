#extrait les mots du fichiers

'''with open("prenoms.txt", "r") as f:
    print(f.read())'''

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
with open("prenoms.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.replace('\n', ''))
