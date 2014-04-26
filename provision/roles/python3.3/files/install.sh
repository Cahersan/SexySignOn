cd /tmp
wget http://python.org/ftp/python/3.3.3/Python-3.3.3.tar.bz2
tar xf Python-3.3.3.tar.bz2
cd Python-3.3.3
./configure --prefix=/usr
make && sudo make altinstall
