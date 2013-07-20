# -*- coding: utf-8 -*-
# palestra relampago - pugpe - download de media com python

import urllib
import urllib2
import requests

# hino do brasil
url = 'http://www.dominiopublico.gov.br/pesquisa/DetalheObraDownload.do?select_action=&co_obra=2486&co_midia=3'

r = requests.get(url)
with open('download-requests.mp3', 'wb') as f:
    for chunk in r.iter_content():
            f.write(chunk)

# download-urllib2.mp3
arquivo = urllib2.urlopen(url)
output = open('download-urllib2.mp3', 'wb')
output.write(arquivo.read())
output.close()

# download-urlretrieve.mp3
urllib.urlretrieve(url, "download-urlretrieve.mp3")
