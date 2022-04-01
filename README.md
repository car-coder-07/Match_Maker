# Match_Maker

Matches your Tinder profile with the person who liked you.

# tinder.user.js

tinder.user.js is forked from https://gist.github.com/Tajnymag/9de74305f9bb09aa940d26418bd508f1#file-tinder-user-js


Run this .js script in the console of the Tinder webpage using Inspect to deblur the profile image of the person in the Matches section who liked you and save it for feature comparision using TinderMatchMaker.py

# TinderMatchMaker.py 

Open the Tinder website and run the TinderMatchMaker.py in Python IDE of your choice in the minimised display format.


Make sure it does not cover the Tinder profile area on the display screen.


This script compares the features of the image that you previously saved from the Matches section with the profile images and looks for the particular match using FLANN based Matcher.


If the potential match is found it likes the image and makes a Tinder match. Otherwise, it will dislike and check further profiles.


Check for the dimensions of your display and the location of the like, dislike and next image icons in the display and edit those positions in the TinderMatchMaker.py script if necessary.


# Note: Interrupt the Loop using sleep command.

