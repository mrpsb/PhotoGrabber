from imgurpython import ImgurClient
from imgurkey import *
import urllib
import os

# Connect to Imgur
# Grab the first page of most recent images for srcreddits
# Download (if not already grabbed)

imgur = ImgurClient(IMGUR_CLIENT_ID,IMGUR_CLIENT_SECRET)

imgs = []
u = urllib.URLopener()

srcreddits = ('EarthPorn','LavaPorn','AbandonedPorn','F1Porn',
		'ThingsCutInHalfPorn','SpaceFlightPorn', 'GeekPorn','SpacePorn')

for sub in srcreddits:
	print "Getting Most Recent Images From Subreddit: r/" + sub
	imgs += imgur.subreddit_gallery(sub, sort='time', window='day', page=0)
	
for img in imgs:

    if img.is_album == True:
        for i in img:
            if i.width > i.height:
                print "Downloading from album"
                u = urllib.URLopener()
                file = i.link.split('/')[-1]
                if os.path.isfile('/home/pi/Pictures/' + file):
		    print "File already exists" 
		else:
		    print "Downloading " + i.link + " to file " + i.link.split('/')[-1]
                    u.retrieve(img.link,"/home/pi/Pictures/" + file)

    else:
        if img.width > img.height:
            file = img.link.split('/')[-1]
            if os.path.isfile('/home/pi/Pictures/' + file):
                print "File already exists: " + img.link
            else:
		u = urllib.URLopener()
                print "Downloading " + i.link + " to file " + i.link.split('/')[-1]
                u.retrieve(img.link,"/home/pi/Pictures/" + file)

