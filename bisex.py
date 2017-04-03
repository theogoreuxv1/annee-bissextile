annee = input("entrez une année")
annee = int(annee)
bisextile = False

if annee % 400 == 0:
        bisextile = True
elif annee % 100 == 0:
        bisextile = False
elif annee % 4 == 0:
        bisextile = True
else:
        bisextile =False

if bisextile:
        print("Votre année est bisextile")
else:
        print("Votre année n'est pas bisextile")
