#!/usr/bin/python

import imgurpython
import random
# import subprocess
import sys

client_id = '3858e09e11ce18d'
client_secret = 'fd9ce9914d9e98815f9dda6af65f1cd2623c2dad'
args = sys.argv

del args[0]

query = ''
for argument in args:
    query += argument + ' '

# print 'Search Terms: {0}'.format(query)

client = imgurpython.ImgurClient(client_id, client_secret)
items = client.gallery_search(query, advanced=None, sort='time', window='all', page=0)
random = random.randint(0, len(items))

# print 'Array Length: {0}'.format(len(items))
# print 'Random Image: {0}'.format(random)

if len(items) == 0:
    print 'No matches'
    exit(0)
else:
    url = items[random].link

print '{0}'.format(url)

# subprocess.Popen(['open', url])
