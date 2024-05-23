# Nom = "YAHAYA"
# Prenom = " Usman"
# Nom_complet = Nom + Prenom

# print(Nom_complet[6:10])


# location_de_voiture =  {'Nom' : 'Mercedez benz 2022', 'Couleur':'Blanche'}

# for keys in location_de_voiture:
#     print(location_de_voiture[keys])

# print("Voiture selectioner est : " + location_de_voiture['Nom'] + " et est de couleur : " + location_de_voiture['Couleur'])

# List = [1,2,3,4,5,6,7,8]
# for number in List:
#     print(number%2 == 0)

# def function(a,b,c):
#     return a + b + c

# sum = function(12,23,43) + function(20,43,10)
# print(sum)


import random

# def function1():
#     a = random.choice(range(1,100))
#     b = random.choice([200, 300])
#     c = random.randint(0, 1000)
#     return a, b , a+b

# print(function1())

def aleatoire(bool, list, min, max):
    if bool == True:
        x = random.choice(list)
        return x
    else:
        y = random.randint(min, max)
        return y
    
print(aleatoire(True,[1,2,3,4,5],0,100))
print(aleatoire(False, [], 0, 300))





# math = random.randint(3,10)
# print(math)

