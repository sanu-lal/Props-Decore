import urllib.request
from urllib.error import HTTPError
import re

try:
    urllib.request.urlopen('http://127.0.0.1:8000/')
except HTTPError as e:
    content = e.read().decode('utf-8')
    m = re.search(r'<div id="summary">(.+?)</div>', content, re.DOTALL)
    if m:
        text = re.sub(r'<[^>]+>', ' ', m.group(1))
        # Compress whitespace
        text = re.sub(r'\s+', ' ', text)
        print(text[:3000].strip())
    else:
        print("No summary found")
