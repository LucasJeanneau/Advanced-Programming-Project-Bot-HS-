from blizzardapi import BlizzardApi as bz
from PIL import Image
import requests
from io import BytesIO
import os

## Set working directory

os.chdir('/Users/Lucas/Desktop/HS_Project/IM_TAUNT')

## Download taunt images

# API identifiants 
client = bz("a715d9d9be4b4677868822a101d00a03", "vf2uZOh4tDSa7FpTTx0S56KJgCQ0xscp")

# I first download all taunt minions cards by using the keyword "taunt"

param = {"keyword": "taunt", "pageSize" : "600", "set": "standard", 'type':'minion'}

cards_taunt = client.hearthstone.game_data.search_cards("eu", "fr_FR", **param)
# The API return a dict "cards_taunt" which contains 4 keys (cardCount, cards, page and pageSize)

info = cards_taunt['cards']
# I only keep the key "cards" which contain all informations I needed

list_link = []
# create an empty list

for i in info:
    list_link.append(i['image'])
# fill the list with links which allow to get images of each card

name=1

for link in list_link:
    img_data = requests.get(link).content
    with open(str(name)+'.png','wb') as handler:
       handler.write(img_data)
    name+=1

## Download images of all cards with the same process

os.chdir('/Users/Lucas/Desktop/HS_Project/IM_ALL')

param = {"pageSize" : "500", "set": "standard", 'type':'minion','page':'1'}

cards_taunt = client.hearthstone.game_data.search_cards("eu", "fr_FR", **param)

info = cards_taunt['cards']

list_link = []

for i in info:
    list_link.append(i['image'])

name=1

for link in list_link:
    img_data = requests.get(link).content
    with open(str(name)+'.png','wb') as handler:
       handler.write(img_data)
    name+=1
    
param = {"pageSize" : "500", "set": "standard", 'type':'minion','page':'2'}

cards_taunt = client.hearthstone.game_data.search_cards("eu", "fr_FR", **param)

info = cards_taunt['cards']

list_link = []

for i in info:
    list_link.append(i['image'])

name=501

for link in list_link:
    img_data = requests.get(link).content
    with open(str(name)+'.png','wb') as handler:
       handler.write(img_data)
    name+=1