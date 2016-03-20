# PhotoGrabber

Dead simple Python script for Raspberry Pi using the imgurpython library for Imgur's API
Downloades images from the specified subreddit's Imgur gallery front page into default pi user's Pictures dir

Rename imgurkey_blank.py to imgurkey.py
Get an Imgur API key (you only need an anon one) and put the Client ID and Client Secret in imgurkey.py

To change the subreddits you're grabbing pics from, add/remove names from here:

```
srcreddits = ('EarthPorn','LavaPorn','AbandonedPorn','F1Porn',
                'ThingsCutInHalfPorn','SpaceFlightPorn', 'GeekPorn','SpacePorn')
```

The script discards pics higher than they are wide (as the display I'm using to display is landscape 800x480)
