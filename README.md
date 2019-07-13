# DBD Icon Maker
---

A Python script to create custom perk icons for Dead By Daylight.

#Usage
---
`python dbdIconMaker.py <1 to copy perks into game files, 0 to do it manually> "<Path to DBD>"  "Name of background image"`

Example:
`python dbdIconMaker.py 1 "C:\Program Files (x86)\Steam\steamapps\common\Dead by Daylight" "rainbow.jpg"`


#Requirements
---
Requires [ImageMagick](https://imagemagick.org/script/download.php). Install for your OS.
Requires Python 3.
Requires Wand (use `pip install Wand')

Make sure you enter the correct path for DBD to avoid losing game files. A backup called 'Perks.zip' is created when running. Extract to `C:\Program Files (x86)\Steam\steamapps\common\Dead by Daylight\DeadByDaylight\Content\UI\Icons\Perks` to restore.
