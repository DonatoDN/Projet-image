import pygame
import sys
import os
import random
import time
from config import Config
from pygame.locals import *
import json
from datetime import datetime

start_date_str = Config.start_dt
end_date_str = Config.end_dt
start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
difference = start_date - end_date
nb_seconds = difference.total_seconds()

path = os.path.join('app','config.py', Config.coords_file)
json_file = open(path,'r')
json_string = json_file.read()
json_file.close()

tuple_coords = [tuple(coords) for coords in json.loads(json_string)]


def quit():
    pygame.quit()
    sys.exit()

def main():
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
        
    nb_pixels = Config.SCREEN_HEIGHT * Config.SCREEN_WIDTH
    
    print("nb pixels", nb_pixels)
        
    # Start the main loop
    while True:
        # Get events from the event queue
        for event in pygame.event.get():
            # Check for the quit event
            if event.type == pygame.QUIT:
                quit()
            
            if event.type == pygame.KEYUP:
                # quit when Q is pressed
                if event.key == K_q:
                    quit()

        for _ in range(10000):
            x = random.randint(0, Config.SCREEN_WIDTH - 1)
            y = random.randint(0, Config.SCREEN_HEIGHT - 1)
                        
            color = surf2.get_at((x, y))
            
            surf1.set_at((x, y), color)
            

        # Update the game state
        display.blit(surf1, (0, 0))
        
        # Draw the game screen
        pygame.display.update()

        # Limit the FPS by sleeping for the remainder of the frame time
        clock.tick(Config.desired_fps)
        
main()

#selctionner pixels pour changer en couleur (prog du prof)
#créer des frames précises avec un changement d'un certains nombres de pixels précis
#faire le backup