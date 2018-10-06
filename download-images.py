from bs4 import BeautifulSoup

import requests

URL = "http://www.nationalgeographic.com.cn/animals/"

html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_url_list = soup.find_all('ul', {'class': 'img_list'})

for item in img_url_list:
    imgs = item.find_all('img')
    for img in imgs:
        # print(img['src'])
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./imgs/%s'%image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s'%image_name)
