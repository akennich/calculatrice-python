print("=== Ma calculatrice ===")

print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

choix = input("Choisis une opération (1-4) : ")
nombre1 = float(input("Entre le premier nombre : "))
nombre2 = float(input("Entre le deuxième nombre : "))
if choix == "1":
    resultat = nombre1 + nombre2
    print("Résultat :", resultat)

elif choix == "2":
    resultat = nombre1 - nombre2
    print("Résultat :", resultat)

elif choix == "3":
    resultat = nombre1 * nombre2
    print("Résultat :", resultat)

elif choix == "4":
    if nombre2 == 0:
        print("Impossible de diviser par zéro !")
    else:
        resultat = nombre1 / nombre2
        print("Résultat :", resultat)

else:
    print("Choix invalide")
  

