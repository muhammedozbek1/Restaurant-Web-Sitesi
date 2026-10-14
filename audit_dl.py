import re, os, urllib.request
base = os.path.join(os.environ.get('TEMP', '/tmp'), 'myra_audit')
os.makedirs(base, exist_ok=True)
html = open('index.html', encoding='utf-8').read()
ms = re.findall(r'\{id:(\d+),\s*name:"([^"]+)",\s*cat:"([^"]+)".*?img:"([^"]+)"', html)
print(f"found {len(ms)}")
for pid, name, cat, url in ms:
    ext = 'jpg'
    fp = os.path.join(base, f"{int(pid):02d}_{cat}.{ext}")
    try:
        urllib.request.urlretrieve(url, fp)
        print(f"OK {pid} {name}")
    except Exception as e:
        print(f"FAIL {pid} {e}")
