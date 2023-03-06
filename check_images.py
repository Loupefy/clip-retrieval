from PIL import Image
import os

i = 0

for root, dirs, files in os.walk("images", topdown=False):
    for name in files:
        try:
            Image.open(os.path.join(root, name))
        except:
            os.remove(os.path.join(root, name))
            i += 1
            print(i)
            
print(i)