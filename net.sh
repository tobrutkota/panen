#!/bin/bash

# Bersihin proxychains sebelumnya biar fresh
rm -rf ~/proxychains

# Buat folder baru
mkdir -p ~/proxychains && cd ~/proxychains
wget https://github.com/rofl0r/proxychains-ng/archive/refs/heads/master.zip

unzip master.zip && rm master.zip && cd proxychains-ng-master

./configure --prefix=$HOME/.local && make && make install

mkdir -p ~/.proxychains

# Salin config default buat dihapus biar bersih
cp ~/proxychains/proxychains-ng-master/src/proxychains.conf ~/.proxychains/proxychains.conf

# Bersihin config lama
rm -f ~/.proxychains/proxychains.conf

# Buat config baru dengan proxy rotate
cat <<EOF > ~/.proxychains/proxychains.conf
strict_chain
proxy_dns
random_chain
tcp_read_time_out 15000
tcp_connect_time_out 8000
[ProxyList]
socks5 38.154.227.167 5868 mnlfbonv oz70qvg3eznw
socks5 38.153.152.244 9594 mnlfbonv oz70qvg3eznw
socks5 173.211.0.148 6641 mnlfbonv oz70qvg3eznw
socks5 23.94.138.75 6349 mnlfbonv oz70qvg3eznw
socks5 64.64.118.149 6732 mnlfbonv oz70qvg3eznw
socks5 166.88.58.10 5735 mnlfbonv oz70qvg3eznw
EOF

chmod 600 ~/.proxychains/proxychains.conf

echo "ProxyChains Udah Bersih + Rotate + Licin 🔥💋 Siap panen buat beli rumah di Bali sayang 😘"
