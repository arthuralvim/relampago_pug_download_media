# -*- coding: utf-8 -*-
# palestra relampago - pugpe - download de media com python

from urllib2 import urlopen

broken = open('trio-nordestino-musicas-urls-broken.txt', 'w')
with open('trio-nordestino-musicas-urls.txt', 'r') as txt:
    for counter, line in enumerate(txt):
        print ' -> Music', counter
        url = line.strip()
        try:
            code = urlopen(url).code
        except Exception, e:
            print url
            broken.write('{0}\n'.format(url))
broken.close()
