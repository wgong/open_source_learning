import shutil
for i in range(3,27):
	shutil.copy2("%d.jpg"%i,  "A-%02d.jpg"%(i-2))