import os
import json
import random

w = 3840
h = 2160

coords = [(x,y) for x in range(w) for y in range(h)]
random.shuffle(coords)

filepath = os.path.join('app','coords.json')
with open(filepath,'w') as coords_file:
    coords_file.write(json.dumps(coords))

