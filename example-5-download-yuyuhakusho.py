# -*- coding: utf-8 -*-
# palestra relampago - pugpe - download de media com python

import urllib
import json
import urlparse
import subprocess

author = 'caiotpv'

foundAll = False
ind = 1
videos = []
while not foundAll:
    inp = urllib.urlopen(r'http://gdata.youtube.com/feeds/api/videos?start-index={0}&max-results=50&alt=json&orderby=published&author={1}'.format(ind, author))
    try:
        resp = json.load(inp)
        inp.close()
        returnedVideos = resp['feed']['entry']
        for video in returnedVideos:
            videos.append(video)

        ind += 50
        print len(videos)
        if (len(returnedVideos) < 50):
            foundAll = True
    except:
        #catch the case where the number of videos in the channel is a multiple of 50
        print "error"
        foundAll = True

for video in videos:
    print video['title']['$t']  # video title
    filename = video['title']['$t']
    yt_url = video['link'][0]['href']
    yt_url_data = urlparse.urlparse(yt_url)
    query = urlparse.parse_qs(yt_url_data.query)
    yt_video_id = query["v"][0]

    # subprocess.call(['youtube-dl', '-o', '%(title)s.%(ext)s', yt_video_id])

    # just a demonstration...
    filezinho = open(filename, 'w')
    filezinho.write(yt_url)
    filezinho.write(yt_video_id)
    filezinho.close()


subprocess.call(['youtube-dl', '-o', '%(title)s.%(ext)s', yt_video_id])
# http://en.wikipedia.org/wiki/YouTube#Quality_and_codecs
# http://rg3.github.io/youtube-dl/documentation.html

print 'Arigatou gozaimasu!'
