# -*- coding: utf-8 -*-
# palestra relampago - pugpe - download de media com python

import re
import urllib
# wget forked from https://bitbucket.org/techtonik/python-wget/src
import wget
from BeautifulSoup import BeautifulSoup

print '=> Abrindo site do Trio Nordestino...'

# get all albuns.
albuns = []

print '=> Get albuns for 1 page.'
url = 'http://www.trionordestino.com.br/?page_id=27'
f = urllib.urlopen(url)
soup = BeautifulSoup(f)
album = soup.findAll('a', attrs={'href': re.compile(r'\?audio=[\w-]+')})
albuns = album + albuns

for i in range(2, 6):
    print '=> Get albuns for {0} page.'.format(str(i))
    url = 'http://www.trionordestino.com.br/?page_id=27&paged={0}'.format(str(i))
    f = urllib.urlopen(url)
    soup = BeautifulSoup(f)
    album = soup.findAll('a', attrs={'href': re.compile(r'\?audio=[\w-]+')})
    albuns = album + albuns

# save urls from albuns
with open('trio-nordestino-albuns-urls.txt', 'wb') as txt:
    for alb in albuns:
        txt.write(u'{0}\n'.format(alb['href']))

# entering in each album and get each music
all_musics = []
all_covers = []
with open('trio-nordestino-albuns-urls.txt', 'r') as txt:
    for counter, line in enumerate(txt):
        print str(counter + 1), 'Album extracted.'
        url = line.strip()
        f = urllib.urlopen(url)
        soup = BeautifulSoup(f)
        musics = soup.findAll('a', attrs={'data-src': re.compile(r'.mp3$')})
        all_musics = musics + all_musics

        over_cover = soup.find('div', attrs={'class': 'audio-single-cover'})
        cover = [over_cover.find('img')]
        all_covers = cover + all_covers

# save urls from musics
with open('trio-nordestino-musicas-urls.txt', 'wb') as txt:
    for mus in all_musics:
        txt.write('{0}\n'.format(mus['data-src']))

# save urls from covers
with open('trio-nordestino-capas-urls.txt', 'wb') as txt:
    for cov in all_covers:
        txt.write('{0};{1}\n'.format(cov['src'], cov['alt'].encode('utf-8')))

# prepare for download
downloads = []
downloads_cover = []
with open('trio-nordestino-musicas-urls.txt', 'r') as txt:
    for counter, line in enumerate(txt):
        url = line.strip()
        album = url.split('/')[-2]
        music = url.split('/')[-1]
        filename = u'{0}-{1}'.format(album, music)
        downloads.append((url, filename))

with open('trio-nordestino-capas-urls.txt', 'r') as txt:
    for counter, line in enumerate(txt):
        url = line.strip().split(';')[0]
        filename = '{0}.jpg'.format(line.strip().split(';')[1])
        downloads_cover.append((url, filename))

filenames = [name for (url, name) in downloads]
filenames_covers = [name for (url, name) in downloads_cover]
if len(filenames) != len(set(filenames)) and len(filenames_covers) != len(set(filenames_covers)):
    print u'Sorry bro. You have some duplicates...'
else:
    print u'Ok for download.'

# download
for counter, download in enumerate(downloads):
    print u' {0} - {1} -> {2}'.format(str(counter), download[0], download[1])
    filename = wget.download(download[0], download[1])

for counter, download in enumerate(downloads_cover):
    print ' {0} - {1} -> {2}'.format(str(counter), download[0], download[1])
    filename = wget.download(download[0], download[1])

# Forró time!
