from rdoclient import RandomOrgClient
from os import listdir, remove
from os.path import isdir, join, splitext, exists
from shutil import copyfile

r = RandomOrgClient('API KEY')

dirs = [d for d in listdir() if isdir(d)]
imgs = [join(d, i) for d in dirs for i in listdir(d)]
image_number = r.generate_integers(1, 0, len(imgs))[0]
image = imgs[image_number]

daily_image_location = "/home/zar/Desktop/Daily Asana"

if exists(daily_image_location+'.png'):
    remove(daily_image_location+'.png')
if exists(daily_image_location+'.jpg'):
    remove(daily_image_location+'.jpg')

copyfile(image, daily_image_location+splitext(image)[1])

