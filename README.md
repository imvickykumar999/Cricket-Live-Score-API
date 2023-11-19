> # `Cricket Live Score`
>
> ![image](https://github.com/imvickykumar999/Cricket-Live-Score-API/assets/50515418/196ca5ef-e75d-4e25-badc-3e289d33a0e7)

<br>

```python
import requests
from bs4 import BeautifulSoup as bs

link = 'https://static.cricinfo.com/rss/livescores.xml'
req = requests.get(link)

soup = bs(req.content, 'xml')
box = soup.findAll('title')

for i in box:
    if 'india' in i.text.lower():
        print(i.text)
```

```bash
>>> python cric_live_score.py
India 240/10  v Australia 63/3 *
```

<br>

![image](https://github.com/imvickykumar999/Cricket-Live-Score-API/assets/50515418/044ad657-02ac-420d-91d9-38b0bf0640f8)
