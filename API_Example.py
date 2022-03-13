# -*- coding: utf-8 -*-
"""
@author: Jason Harris
"""

import requests                                                         # importing requests module
import json

url = "https://pokeapi.co/api/v2/"
result = requests.get(f"{url}/pokemon/pikachu")                         # The URL for the pikachu pokemon api
species = "species"
evo = "evolution_chain"

if result:
  print('Request is successful.')
else:
  print('Request returned an error.')

print(type(result.json()))

def jprint(obj):                                                        # to print the contents of the json
    text = json.dumps(obj, sort_keys=True, indent=4)                    # create a formatted string of the Python JSON object
    print(text)

type = " "                                                              # Making a variable to hold the species URL
result_data = result.json()                                             # assigning the pikachu json to a variable

for i in result_data:                                                   # iterate through the json to look for species
    if i == species in result_data:
        print("Species exists at", i)
        # print(result_data[i])                                           # found the data
        typed = result_data[i]                                          # creating a list of the dict data
        type = typed["url"]                                             # assigning the data to a variable
        print(type)                                                     # verifying the data

r2 = requests.get(f"{type}")                                            # assign the species data page to a dict

if r2:                                                                  # verifying the url is query-able    
  print('Request is successful.')
else:
  print('Request returned an error.')

type2 = " "                                                             # making a variable to hold the evolution URL
r2_data = r2.json()                                                     # assigning the species json to a variable

for i in r2_data:                                                       # iterating through the specis json searching for evo data
    if i == evo in r2_data:
        print("Evolution data exists at", i)                            # found it
        # print(r2_data[i])                                               # printing it for all to see
        typed2 = r2_data[i]                                             # creating the list of evolution data
        type2 = typed2["url"]                                           # assigning it to a variable
        print(type2)                                                    # verifying the data in the variable

r3 = requests.get(f"{type2}")                                           # assigning the dict to a variable
jprint(r3.json())                                                       # printing the json of all evolution data in the "Pikachu Lineage"
pika = r3.json()["chain"]["species"]
pika_name = pika["name"]
pika_url = pika["url"]
print("\n")
print(pika_name, "is the baby form, and can be found at", pika_url)
pikachu = r3.json()["chain"]["evolves_to"][0]["species"]
pikachu_name = pikachu["name"]
pikachu_url = pikachu["url"]
print(pikachu_name, "is the first evolution, and can be found at", pikachu_url)
raichu = r3.json()["chain"]["evolves_to"][0]["evolves_to"][0]["species"]
raichu_name = raichu["name"]
raichu_url = raichu["url"]
print(raichu_name, "is the next level of evolution, and can be found at", raichu_url, "\n")
        
length = len(result_data)        
print(length, "is the number of records available at", url)
lenr2 = len(r2_data)
print(lenr2, "is the number of records available at", type, "- aka Pikachu.")
lenr3 = len(r3.json())
print(lenr3, "is the number of records available at", type2, "-aka the Pika evolution chain.")
