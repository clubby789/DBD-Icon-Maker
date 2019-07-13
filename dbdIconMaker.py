import os, zipfile, sys
from wand.image import Image
from wand.display import display
from distutils.dir_util import copy_tree

def zipdir(path, ziph):
	for root,dirs,files in os.walk(path):
		for file in files:
			ziph.write(os.path.join(root, file))

if len(sys.argv) < 4:
	print("Wrong number of arguments")
	quit()
copyback = sys.argv[1]
dbdpath = sys.argv[2]
background = sys.argv[3]

dbdpath = os.path.join(dbdpath, 'DeadByDaylight/Content/UI/Icons/Perks')
basepath = os.path.dirname(os.path.realpath(__file__))
copyDir = os.path.join(basepath,'Perks')
copy_tree(dbdpath,copyDir)

zipf = zipfile.ZipFile('Perks.zip','w', zipfile.ZIP_DEFLATED)
zipdir('Perks', zipf)
zipf.close()

dirs = []

for filename in os.listdir('Perks'):
	with Image(filename=background) as bg:
		bg.resize(256,256)
		path = os.path.join(basepath,"Perks",filename)
		if os.path.isdir(path):
			dirs.append(path)
			continue
		with Image(filename="Perks/"+filename) as fg:
			bg.composite(fg,left=0,top=0)
			bg.save(filename="Perks/"+filename)

for directory in dirs:
	for filename in os.listdir(directory):
		with Image(filename=background) as bg:
			bg.resize(256,256)
			path = os.path.join(directory,filename)
			with Image(filename=path) as fg:
				bg.composite(fg,left=0,top=0)
				bg.save(filename=path)

if int(copyback) == 1:
	print("Copying back")
	copy_tree(copyDir,dbdpath)