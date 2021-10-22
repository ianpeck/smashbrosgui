import os
path = '/Users/ianjpeck/Documents/GitHub/smashbrosgui/stagepictures'
files = os.listdir(path)
from PIL import Image

for file in files:
    if '.jpeg' in file:
        im1 = Image.open(os.path.join(path, file))
        im1.save(os.path.join(path, file.replace('.jpeg','.png')))

# for file in files:
#     new_file = file.replace('1200px-','').replace('1600px-','').replace('SSBU','').replace('SSBB','').replace('_Stage','').replace("'",'').replace('-','').replace('_','').replace(',','').replace('é','e').lower()
#     print(file, new_file)
#     os.rename(os.path.join(path, file), os.path.join(path, new_file))


# for file in files:
#     new_file = file.replace(".large",'').replace('-dlc','')
#     # index = new_file.index('-') + 1
#     # new_file = new_file[index:len(new_file)].replace('-','')
#     # os.rename(os.path.join(path, file), os.path.join(path, new_file))
    