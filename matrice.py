def remplir_matrice(N, P):
    if N <= 0 or P <= 0 or N > 10 or P > 10:
        print("Les valeurs de N et P doivent être > 0 et ≤ 10.")
        return

    matrice = [[0] * P for _ in range(N)]

    valeur = 1
    for i in range(N):
        for j in range(P):
            matrice[i][j] = valeur
            valeur += 1

    print("Affichage normal:")
    for i in range(N):
        print(matrice[i])

    print("\nAffichage alternatif:")
    for i in range(N):
        if i % 2 == 0:
            print(matrice[i])
        else:
            print(matrice[i][::-1])


N = int(input("Saisire l' entier N :"))
P = int(input("Saisire l' entier P :"))
remplir_matrice(N, P)