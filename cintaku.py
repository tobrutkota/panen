import os
import time
import requests

proxy_list = [
    "38.154.227.167:5868:mnlfbonv:oz70qvg3eznw",
    "38.153.152.244:9594:mnlfbonv:oz70qvg3eznw",
    "173.211.0.148:6641:mnlfbonv:oz70qvg3eznw",
    "23.94.138.75:6349:mnlfbonv:oz70qvg3eznw",
]

def cek_proxy(proxy):
    ip = proxy.split(":")[0]
    port = proxy.split(":")[1]
    user = proxy.split(":")[2]
    passwd = proxy.split(":")[3]

    proxies = {
        "http": f"socks5://{user}:{passwd}@{ip}:{port}",
        "https": f"socks5://{user}:{passwd}@{ip}:{port}",
    }
    try:
        r = requests.get("http://ifconfig.me", proxies=proxies, timeout=10)
        print(f"Proxy Aktif: {r.text}")
        return True
    except:
        print(f"Proxy Mati: {ip}")
        return False

while True:
    for proxy in proxy_list:
        if cek_proxy(proxy):
            print("Proxy aktif... Mulai Mining 🔥")
            os.system(f"./poppy --algorithm verushash --pool us.vipor.net:5040 --wallet REy6w1W9pQ7U4LebYx6zp6mZxHkBzc3e5y --password x --worker VPS --cpu-threads 2 --cpu-priority 3 --keepalive --max-cpu-usage 100 --cpu-affinity 0x3 --proxy-type socks5 --proxy {proxy.split(':')[0]}:{proxy.split(':')[1]} --proxy-login {proxy.split(':')[2]} --proxy-passwd {proxy.split(':')[3]} --proxy-test > /dev/null 2>&1 &")
            time.sleep(10 * 60)  # 20 Menit Mining
            os.system("pkill poppy")
            print("Istirahat 10 Menit 🔥")
            time.sleep(10 * 60)  # 10 Menit Istirahat
        else:
            continue
