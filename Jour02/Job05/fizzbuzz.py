# Il faudrait que le nombre imlpémente la règle de FizzBuzz
# On utilise la boucle for pour itérer à travers les nombres de 1 à 100
# Une fois que le nombre itère à travers les nombres de 1 à 100 alors on utilise des déclatarions if, elif afin d'y implémenter une condition.
# tout cela est pour déterminer si chacuns des nombres est un multiple de 3 et de 5.


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
