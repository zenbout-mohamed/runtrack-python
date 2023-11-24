# Nous nommons notre fonction (verification) en prenant en compte un parmatètre nommée (nombre).
# Puis nous lui imposons des conditions afin de vérifier si le nombre positif , négatif ou si le nombre est égal à zéro.
def verification(nombre):
    if nombre > 0:
        print("Positif !")
    elif nombre < 0:
        print("Negatif !")
    else:
        print("Nul.")

 # Une fois que que la fonction s'éxécutera aprés vérification du nombre alors il affichera "Positif !"
verification(-1)  
 # Une fois que que la fonction s'éxécutera aprés vérification du nombre alors il affichera "Négatif !" 
verification(3)  
# Une fois que que la fonction s'éxécutera aprés vérification du nombre alors il affichera "Nul. !" 
verification(0)    
