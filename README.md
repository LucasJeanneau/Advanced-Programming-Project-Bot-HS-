# Advanced-Programming-Project-Bot-HS-
A Bot that play a predefined Hearthstone deck

#
This project’s is to make a bot able to play a game of Hearthstone (https://playhearthstone.com/fr-fr) with a predefined deck. The deck will be an aggro druid deck (deck that takes an 'aggressive' approach of dealing damage to the opponent as quickly as possible). The bot will play minions and spells from hand by using all available mana each turn and will only attack the enemy hero (never trade opposant’s minion, except if they are taunt). 
The project is separated in 3 different parts/scripts. 

#
First part (script Get_images_from_API) is dedicated to get images of all Hearthstone cards from the Blizzard’s API to use them to detect cards on the game board. I’ll also make another specific request to the API to get only taunt cards, because we’ll need them in a separate folder for the bot.

#
Second part (script Crop_images) will consist in crop all images (changing size and keep only the part of the card that is visible when played) to be detectable on Hearthstone’s board (opencv2 is only able to recognize image of the same size on the screen).

#
And the last part (Bot_HS) is the Bot himself that will recognize cards, play them, and use them to attack the enemy hero (or taunt minions). It’s using pyautogui to make mouse movement/click.
The replication of the project is possible but need extra folder (containing for example screenshot of mana crystals) to work properly (just ask me if you want to access them). 

