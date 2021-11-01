import pyautogui
import time
import cv2
from PIL import Image
import os
from tqdm import tqdm
from joblib import Parallel, delayed



## move to HS and start a game

pyautogui.moveTo(x=700, y=1059)
pyautogui.click()

i = Image.open("img.png")
a = pyautogui.locateOnScreen(i, confidence = 0.7)

if a is not None:
    pyautogui.moveTo(x=1393, y=908)
    pyautogui.click()

time.sleep(50)

pyautogui.moveTo(x=943, y=859)
pyautogui.click()


im = pyautogui.screenshot()

## get color of the "end turn button"

color_screen=im.getpixel((1574, 473))

can = pyautogui.pixelMatchesColor(1574,473,(150,174,1),tolerance=100)

cannot = pyautogui.pixelMatchesColor(1574,473,(26, 169, 1),tolerance=100)

opponent = pyautogui.pixelMatchesColor(1574,473,(54, 69, 73),tolerance=100)

game_finish = pyautogui.pixelMatchesColor(1055,1016,(255,255,255),tolerance=100)

def play_card():
    
  for i in range(len(cards_playable)):
            pyautogui.moveTo(cards_playable[i])
            pyautogui.click()
            pyautogui.dragTo(650, 400, button='left')
            time.sleep(1)
    
def trade_taunt():
        

    path ="C:\\Users\\lucas\\Desktop\\HS_Project\\IM_CROP_TAUNT\\"

    time.sleep(1)

    list_taunt = []
    
    for image in tqdm(os.listdir(path)):
        i = Image.open(path+image)
        a = pyautogui.locateOnScreen(i, confidence = 0.7,region=(340,500,1150,200)) 
        if a is not None:
            minion_coord = [a[0],a[1]]
            list_taunt.append(minion_coord)
    
    if list_taunt is not None:
        
        for taunt in list_taunt:
            for minion in range(len(list_minion)):
                  pyautogui.moveTo(list_minion[minion])
                  pyautogui.click()
                  pyautogui.dragTo(list_taunt[taunt], button='left')
              
def go_face():

        
    for minion in range(len(list_minion)):
          pyautogui.moveTo(list_minion[minion])
          pyautogui.click()
          pyautogui.dragTo(1000, 200, button='left')
          time.sleep(2)
          

def hero_power():
    
    pyautogui.moveTo(x=1135, y=798)
    pyautogui.click()

   
    
def end_turn():
    
     pyautogui.moveTo(x=1564, y=492)
     pyautogui.click()
     
while game_finish==False:
    
    if can==True:        
        
        ## Checking Mana
        
        path ="C:\\Users\\lucas\\Desktop\\HS_Project\\MANA_AVAILABLE\\"


        list_mana = []
    
        for image in tqdm(os.listdir(path)):
            i = Image.open(path+image)
            a = pyautogui.locateOnScreen(i, confidence = 0.8,region=(1210,970,1320,1020)) 
            if a is not None:
                number_mana = int(image[0])
                break
                    
        ## Make action depending on mana available
        
        if number_mana == 1:
             path ="C:\\Users\\lucas\\Desktop\\HS_Project\\MANA\\1\\"

    
             cards_playable = []
        
             for image in tqdm(os.listdir(path)):
                i = Image.open(path+image)
                a = pyautogui.locateOnScreen(i, confidence = 0.7,region=(500, 880, 1300, 1080)) 
                if a is not None:
                    card_coord = [a[0],a[1]]
                    cards_playable.append(card_coord)
                    
            
        
        if number_mana == 2:
             path ="C:\\Users\\lucas\\Desktop\\HS_Project\\MANA\\2\\"

    
             cards_playable = []
        
             for image in tqdm(os.listdir(path)):
                i = Image.open(path+image)
                a = pyautogui.locateOnScreen(i, confidence = 0.7,region=(500, 880, 1300, 1080)) 
                if a is not None:
                    card_coord = [a[0],a[1]]
                    cards_playable.append(card_coord)
                    
            
                
        if number_mana == 3:
             path ="C:\\Users\\lucas\\Desktop\\HS_Project\\MANA\\3\\"

    
             cards_playable = []
        
             for image in tqdm(os.listdir(path)):
                i = Image.open(path+image)
                a = pyautogui.locateOnScreen(i, confidence = 0.7,region=(500, 880, 1300, 1080)) 
                if a is not None:
                    card_coord = [a[0],a[1]]
                    cards_playable.append(card_coord)
                    
            
        
            
        if number_mana == 4:
             path ="C:\\Users\\lucas\\Desktop\\HS_Project\\MANA\\4\\"

             time.sleep(1)
    
             cards_playable = []
        
             for image in tqdm(os.listdir(path)):
                i = Image.open(path+image)
                a = pyautogui.locateOnScreen(i, confidence = 0.7,region=(500, 880, 1300, 1080)) 
                if a is not None:
                    card_coord = [a[0],a[1]]
                    cards_playable.append(card_coord)
                    
            
        
        if number_mana > 4:
             path ="C:\\Users\\lucas\\Desktop\\HS_Project\\MANA\\5\\"

             time.sleep(1)
    
             cards_playable = []
        
             for image in tqdm(os.listdir(path)):
                i = Image.open(path+image)
                a = pyautogui.locateOnScreen(i, confidence = 0.7,region=(500, 880, 1300, 1080)) 
                if a is not None:
                    card_coord = [a[0],a[1]]
                    cards_playable.append(card_coord)
                    
                
            
            
        
        play_card()

        path ="C:\\Users\\lucas\\Desktop\\HS_Project\\DECK_DRUIDE\\"


        list_minion = []
    
        for image in tqdm(os.listdir(path)):
            i = Image.open(path+image)
            a = pyautogui.locateOnScreen(i, confidence = 0.7,region=(340,500,1150,200)) 
            if a is not None:
                minion_coord = [a[0],a[1]]
                list_minion.append(minion_coord)
                time.sleep(0.4)
                
        trade_taunt()
        
        go_face()

            
        hero_power()
        
        can = pyautogui.pixelMatchesColor(1574,473,(150,174,1),tolerance=100)
        cannot= pyautogui.pixelMatchesColor(1574,473,(26, 169, 1),tolerance=100)
        opponent = pyautogui.pixelMatchesColor(1574,473,(54, 69, 73),tolerance=100)
  
        time.sleep(1)
        
    if cannot==True:

        end_turn()
    
        can = pyautogui.pixelMatchesColor(1574,473,(150,174,1),tolerance=100)
        cannot= pyautogui.pixelMatchesColor(1574,473,(26, 169, 1),tolerance=100)
        opponent = pyautogui.pixelMatchesColor(1574,473,(54, 69, 73),tolerance=100)
        
    while opponent==True:
        
        
        time.sleep(10)
        
        can = pyautogui.pixelMatchesColor(1574,473,(150,174,1),tolerance=100)
        cannot= pyautogui.pixelMatchesColor(1574,473,(26, 169, 1),tolerance=100)
        opponent = pyautogui.pixelMatchesColor(1574,473,(54, 69, 73),tolerance=100)
     
        