Kivy Crash Course
=================

This repository contains material relating to my Kivy Crash Course youtube series, a set of (mostly) <10m videos walking users through the creation of a first kivy app, followed by a succession of changes and more advanced concepts to let the app use all of kivy's power.

Most video directories contain a few main files. The python is in `before.py` and `after.py`, containing the code at the start and end of the video respectively. You can download and run `before.py` to follow along with the tutorial, or download and run `after.py` to try the code after I've made the tutorial changes. Kv language definitions are in `tutorial.kv`, and if this changes through the video then the initial and final kv files will be `tutorial.kv_before` and `tutorial.kv_after` respectively. If using these, you'll need to rename them appropriately.

Some videos have an associated `notes.txt`, containing any notes I wrote to go with the video. 

Videos
======

You can find a youtube video with all the Kivy Crash Course videos at https://www.youtube.com/playlist?list=SPdNh1e1kmiPP4YApJm8ENK2yMlwF1_edq, or the individual videos are at:

- Video 1: Making a simple app - https://www.youtube.com/watch?v=F7UKmK9eQLY
- Video 2: Building an android apk - https://www.youtube.com/watch?v=t8N_8WkALdE
- Video 3: More interesting widget interactions - https://www.youtube.com/watch?v=-NvpKDReKyg
- Video 4: Kivy language - https://www.youtube.com/watch?v=ZVWAKzR63ig
- Video 5: Mixing python and kivy language - https://www.youtube.com/watch?v=ZmteLworB4E
  
Plans
=====

The following are my direct plans for the next few videos and general ideas for future topics. Feel free to suggest more!

Next videos:

- Video 6: Mixing python and kv via kivy properties
- Video 7: Drawing on the kivy canvas
- Video 6.5 or 7.5 (interlude): The Label widget (via scrollable label)

Future topics:

- Layouts (examples of different ones) 
- Using android apis via p4a 
- Creating a kivy settings panel 
- Creating a standalone package via pyinstaller
