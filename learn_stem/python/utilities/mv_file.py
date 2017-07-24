import glob
import shutil
for f in  glob.glob("100*.jpg"):
    shutil.move(f, "0{}-{}".format(f[0], f[1:]))
    
for f in  glob.glob("?-*.jpg"):
    shutil.move(f, "0{}".format(f))