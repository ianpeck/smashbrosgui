import os
path = '/Users/ianjpeck/Documents/GitHub/smashbrosgui/fighterpictures'
files = os.listdir(path)


# for index, file in enumerate(files):
#     os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))

for file in files:
    new_file = file.replace(".large",'').replace('-dlc','')
    index = new_file.index('-') + 1
    new_file = new_file[index:len(new_file)].replace('-','')
    os.rename(os.path.join(path, file), os.path.join(path, new_file))
    