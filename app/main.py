import pygame
import sys
import os
import random
import time
from config import Config
from pygame.locals import *
import json
from datetime import datetime
from coords import Coords
import math

#calcul date
start_date_str = Config.start_dt
end_date_str = Config.end_dt
start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
difference = start_date - end_date
total_time = difference.total_seconds()

#nombre pixels par seconde
nb_pixels = Config.SCREEN_HEIGHT * Config.SCREEN_WIDTH
frequency = nb_pixels / (total_time * Config.desired_fps)
difference_pixels = nb_pixels - math.floor(frequency) * Config.desired_fps * total_time
nb_changes = Config.desired_fps * total_time

#création du fichier coords.json
Coords()

#utilisation fichier json coords
path = os.path.join('app', Config.coords_file)
json_file = open(path,'r')
json_string = json_file.read()
json_file.close()

tuple_coords = [tuple(coords) for coords in json.loads(json_string)]


def quit():
    pygame.quit()
    sys.exit()

def main(tuple_coords):
    # Create a clock object
    clock = pygame.time.Clock()
    pygame.init()
    display = pygame.display.set_mode(Config.SCREEN_SIZE)
    try:
        imagefile1 = os.path.join('data', Config.image1)
        imagefile2 = os.path.join('data', Config.image2)
        surf1 = pygame.image.load(imagefile1)
        surf2 = pygame.image.load(imagefile2)
    except IOError as e:
        print(f"{str(e)}")
        quit()
        
    print("nb pixels", nb_pixels)
        
    # Start the main loop
    for i in range(nb_changes - 1):
        # Get events from the event queue
        for event in pygame.event.get():
            # Check for the quit event
            if event.type == pygame.QUIT:
                quit()
            
            if event.type == pygame.KEYUP:
                # quit when Q is pressed
                if event.key == K_q:
                    quit()
        
        #changer les pixels un nombre entier de fois
        if tuple_coords:
            for i in range(math.floor(frequency)):
                if tuple_coords:
                    (x, y) = tuple_coords[0]
                    tuple_coords = tuple_coords[1:]

                    color = surf2.get_at((x, y))
                
                    surf1.set_at((x, y), color)
                else:
                    break
        else:
            break
            

        # Update the game state
        display.blit(surf1, (0, 0))
        
        # Draw the game screen
        pygame.display.update()

        # Limit the FPS by sleeping for the remainder of the frame time
        clock.tick(Config.desired_fps)
    
    #rajouter les pixels manquants
    for i in range(difference_pixels):
        if tuple_coords:
            (x, y) = tuple_coords[0]
            tuple_coords = tuple_coords[1:]

            color = surf2.get_at((x, y))
                
            surf1.set_at((x, y), color)
        else:
            break
main(tuple_coords)


#attendre la bonne date pour exécuter
#faire le backup