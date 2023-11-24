# Nous devons pour cela définir une fonction en prenant en compte en paramètre (width et height).
def draw_rectangle(width, height):
    if width <= 0 or height <= 0:
        print("Les dimensions du rectangle doivent être des entiers positifs.")
        return
    for i in range(height):
        if i == 0 or i == height - 1:
            # Première et dernière ligne : afficher une ligne complète de '-'
            print('-' * width)
        else:
            # Autres lignes : afficher '|', espace, et '|' aux extrémités.
            print('|' + ' ' * (width - 2) + '|')
            print('|' + ' ' * (width - 2) + '|')
            print('|' + ' ' * (width - 2) + '|')

# Nous appellons la fonction tout en augmentant ou en diminuant selon notre intermédiaire les valeurs, donc la taille de notre rectangle.
draw_rectangle(10, 3)
