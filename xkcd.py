#!python3
#downloader
import requests, os, bs4
url="https://xkcd.com"
os.makedirs('xkcdComics',exist_ok=True)
while not url.endswith('#'):
    xkp=requests.get(url)
    xkp.raise_for_status()
    html=bs4.BeautifulSoup(xkp.text,"html.parser")
    comicE=html.select('#comic img')
    if comicE==[]:
        print('cannot be found')
    else:
        comicUrl=comicE[0].get('src')
        comicUrl='https:'+comicUrl
        xki=requests.get(comicUrl)
        xki.raise_for_status()
        imageFile=open(os.path.join('xkcdComics',os.path.basename(comicUrl)),'wb')
        for chu in xki.iter_content(100000):
            imageFile.write(chu)
        imageFile.close()
    prevLink=html.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+prevLink.get('href')
