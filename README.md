# PhotoGrabber

Dead simple Python script using the imgurpython library for Imgur's API

Rename imgurkey_blank.py to imgurkey.py
Get an Imgur API key (you only need an anon one) and put the Client ID and Client Secret in imgurkey.py

To change the subreddits you're grabbing pics from, add/remove names from here:

```
srcreddits = ('EarthPorn','LavaPorn','AbandonedPorn','F1Porn',
                'ThingsCutInHalfPorn','SpaceFlightPorn', 'GeekPorn','SpacePorn')
```

The script discards pics higher than they are wide (as the display I'm using is landscape 800x480)
