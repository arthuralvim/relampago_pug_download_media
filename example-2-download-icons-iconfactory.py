# -*- coding: utf-8 -*-
# palestra relampago - pugpe - download de media com python

import re
import urllib
import urlparse
# wget forked from https://bitbucket.org/techtonik/python-wget/src
import wget
from BeautifulSoup import BeautifulSoup

# download candybar here -> http://www.panic.com/blog/2012/08/candybar-mountain-lion-and-beyond

print '=> Open IconFactory URL...'

# get all links.
links = []

print '=> Get links for 1 page.'
url = 'http://iconfactory.com/freeware/icon'
f = urllib.urlopen(url)
soup = BeautifulSoup(f)
newlinks = soup.findAll('a', attrs={'href': re.compile(r'icontainer.dmg$')})
links = links + newlinks

for i in range(2, 41):
    print '=> Get links for {0} page.'.format(str(i))
    url = 'http://iconfactory.com/freeware/icon?page={0}'.format(str(i))
    f = urllib.urlopen(url)
    soup = BeautifulSoup(f)
    newlinks = soup.findAll('a', attrs={'href': re.compile(r'icontainer.dmg$')})
    links = links + newlinks

# save urls
with open('icontainer-urls.txt', 'wb') as txt:
    for li in links:
        full_url = urlparse.urljoin(url, li['href'])
        txt.write(u'{0}\n'.format(full_url))

# prepare for download
downloads = []
with open('icontainer-urls.txt', 'r') as txt:
    for counter, line in enumerate(txt):
        url = line.strip()
        filename = u'{0}-{1}.dmg'.format(str(counter+1), url.split('/')[-2])
        downloads.append((url, filename))

filenames = [name for (url, name) in downloads]
if len(filenames) != len(set(filenames)):
    print u'Sorry bro. You have some duplicates...'
else:
    print u'Ok for download.'

# download
for counter, download in enumerate(downloads):
    print u' {0} - {1} -> {2}'.format(str(counter), download[0], download[1])
    filename = wget.download(download[0], download[1])

# you get all icons!
