# Advanced-Programming-Project-Bot-HS-
A Bot that plays a predefined Hearthstone deck

## Introduction
This project aims to make a bot able to play a game of Hearthstone (https://playhearthstone.com/fr-fr) with a predefined deck. The deck will be an aggro druid deck (a deck that takes an 'aggressive' approach of dealing damage to the opponent as quickly as possible). The bot will play minions and spells from the hand by using all available mana each turn and will only attack the enemy hero (never trade opponent’s minion, except if they are taunted). 
The project is separated into 3 different parts/scripts. 

## I. Using Blizzard's API
The first part (script Get_images_from_API) is dedicated to getting images of all Hearthstone cards from the Blizzard’s API to use them to detect cards on the game board. I’ll also make another specific request to the API to get only taunt cards because we’ll need them in a separate folder for the bot.

## II. Crop cards images
The second part (script Crop_images) will consist of the crop all images (changing size and keeping only the part of the card that is visible when played) to be detectable on Hearthstone’s board (opencv2 is only able to recognize images of the same size on the screen).

## III. The Bot himself
And the last part (Bot_HS) is the Bot himself that will recognize cards, play them, and use them to attack the enemy hero (or taunt minions). It’s using pyautogui to make mouse movements/click.
The replication of the project is possible but needs extra folders (containing screenshot of mana crystals, and cards of the used deck) to work properly (just ask me if you want to access them). 

