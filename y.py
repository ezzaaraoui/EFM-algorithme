def est_Bissextile(annee):
    if ( annee % 4 == 0 and annee % 100 != 0 ) or (annee % 400 == 0):
        return True
    else:
        return False

def Annee_bissextile(siecle):
    Annee_b = [] 
    siecle1 = ((siecle - 1) * 100)
    for _ in range(1, 101):
        siecle1 += 1
        if est_Bissextile(siecle1):
            Annee_b.append(siecle1)
            
    return Annee_b        

Siecle = int(input("Saisire le siecle :"))
print(f"Les annees bissextile du siecle {Siecle} est", Annee_bissextile(Siecle))