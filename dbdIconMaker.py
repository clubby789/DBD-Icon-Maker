import os, zipfile, sys, argparse
from wand.image import Image
from wand.display import display
from distutils.dir_util import copy_tree

def zipdir(path, ziph):
	for root,dirs,files in os.walk(path):
		for file in files:
			ziph.write(os.path.join(root, file))

parser = argparse.ArgumentParser()
parser.add_argument("copyback", help="Should icons be copied back? (0 or 1)", type=int)
parser.add_argument("dbdpath", help="Base DBD path in Steam", type=str)
parser.add_argument("backgroundimage", help="Background image to apply to perks",type=str)
args = parser.parse_args()

copyback = args.copyback
dbdpath = args.dbdpath
background = args.backgroundimage

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