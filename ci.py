import re
import requests
import time

URL = "https://mirror.ghproxy.com/https://raw.githubusercontent.com/joevess/IPTV/main/sources/iptv_sources.m3u8"
raw_content = requests.get(URL).text


records = re.findall(r"group-title=\"(.+?)\"\s+tvg-id=\"(.+?)\"[^\n]+\n([^\n]+)",raw_content)
g2nu = {}
for group,name,url in records:
    g2nu.setdefault(group,[])
    g2nu[group].append([name,url])

for group,nu in g2nu.items():
    print(f"{group},#genre#")
    for name,url in nu:
        print(f"{name},{url}")
    print()
