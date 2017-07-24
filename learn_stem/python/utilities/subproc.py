
from multiprocessing import Process
from time import sleep

def count_sheeps(number):
    """Count all them sheeps."""
    fd=open('C:/tmp/subproc3.log','w')
    for sheep in range(number):
        fd.write("%s " % sheep)
        #sleep(1)
    fd.close()

if __name__ == "__main__":
    count_sheeps(20)
    p = Process(target=count_sheeps, args=(5,))
    p.daemon = True
    p.start()
    print("Let's just forget about it and quit here and now.")
    exit()
