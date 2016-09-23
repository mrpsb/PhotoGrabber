#coding: UTF-8
from imgurpython import ImgurClient
import imgurkey
import urllib
import os

# Connect to Imgur
# Grab the first page of Specified Subreddits
# Download everything

imgur = ImgurClient(imgurkey.IMGUR_CLIENT_ID,imgurkey.IMGUR_CLIENT_SECRET)

imgs = []
u = urllib.URLopener()

srcreddits = (
         'Pics','EarthPorn',
             'LavaPorn','AbandonedPorn',
             'SpacePorn'
             )

for sub in srcreddits:
    print "Getting Most Recent Images From Subreddit: r/" + sub
    imgs += imgur.subreddit_gallery(sub, sort='time', window='day', page=0)

for img in imgs:

    # If an album according to API only cover img available when accessed as gallery
    # Use API get_album method to grab all the images in the album

    if img.is_album == True:
        print "Getting album " + img.id
        i = imgur.get_album(img.id)

        for pix in i.images:

            filename = pix['link'].split('/')[-1]

            #print "Album branch, pix['link'] is " + pix['link'] + " file is " + file

            if int(pix['width']) > int(pix['height']):
                
                if os.path.isfile('/home/pi/Pictures/' + filename):
                    print "Album Branch - File already exists"
                else:
                    print "Downloading album image " + pix['link'] + " to file " + filename
                    u.retrieve(pix['link'],"/home/pi/Pictures/" + filename)
            else:
                continue

        # Otherwise just grab the image

    else:
        if int(img.width) > int(img.height):
            filename = img.link.split('/')[-1]
            if os.path.isfile('/home/pi/Pictures/' + filename):
                print "Image Branch - File already exists: " + filename
            else:
                print "Downloading " + img.link  + " to file " + filename
                u.retrieve(img.link,"/home/pi/Pictures/" + filename)
