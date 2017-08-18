## download latest caffe from github and unzip to ~/caffe-master
cd ~/caffe-master

# switch to root
sudo -i

## cmake build
mkdir build
cd build
cmake ..
make all
make install
make runtest
