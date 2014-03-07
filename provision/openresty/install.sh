tar xzvf ngx_openresty-1.5.8.1.tar.gz
cd ngx_openresty-1.5.8.1/
./configure --with-luajit
make
make install

# copy useful JSON lua util
cd ..
cp JSON.lua /usr/local/openresty/lualib/resty
