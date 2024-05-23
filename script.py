# import requests


# pikachu_data = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

# print(pikachu_data.json()['name'])

# jason_recuperer = pikachu_data.json()

# recuperer = jason_recuperer['name']


# def combat(name1,name2):
#     pikachu_data_1 =  requests.get('https://pokeapi.co/api/v2/pokemon/'+ name1)
#     jason_recuperer1 = pikachu_data_1.json()

#     pikachu_data_2 =  requests.get('https://pokeapi.co/api/v2/pokemon/pikachu ' + name2)
#     jason_recuperer_2 = pikachu_data_2.json()

#     if(jason_recuperer1 != 'pikachu'):
#         if(jason_recuperer1['id'] > jason_recuperer_2['id']):
#             print(jason_recuperer1 + ' a gagner')
#         else :
#             print(jason_recuperer_2 + 'a gagner')
#     else:
#         print('Pikachu a gagner le champion des pokemon')


# print(comba('Pikachu', ''))

# for id x in data.interows()
# for x in list 
import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
