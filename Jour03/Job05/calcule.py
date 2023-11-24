# Ce bloc conditionnel examine la valeur de operator pour déterminer quelle opération mathématique effectuer.
# Les opérations prises en charge sont l'addition (+), la soustraction (-), la multiplication (*), la division (/), et le modulo (%).
# Pour la division et le modulo, des vérifications sont ajoutées pour éviter les erreurs liées à une division par zéro.
# Si l'opérateur n'est pas reconnu, la fonction renvoie un message indiquant que l'opérateur n'est pas reconnu.

def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Vérification pour éviter une division par zéro
        if num2 != 0:
            return num1 / num2
        else:
            return "Pas de division par 0 !"
    elif operator == '%':
        # Vérification pour éviter une opération de modulo par zéro
        if num2 != 0:
            return num1 % num2
        else:
            return "Pas d'opération de modulo par zéro !"
    else:
        return "Opérateur non reconnu"

# 4 appels de la fonction permettant de claculer différentes opérations
result_n_1 = calcule(50, '+', 23)
result_n_2 = calcule(11, '*', 10)
result_n_3 = calcule(450, '/', 5)
result_n_4 = calcule(99, '%', 10)

# Affichage des résultats
print("Résultat n°1 :", result_n_1)
print("Résultat n°2 :", result_n_2)
print("Résultat n°3 :", result_n_3)
print("Résultat n°4 :", result_n_4)
