"""example from i don't remember where"""

import urllib
import StringIO


# fonction de remplacement
def fakeopen(url, data=None):
    res = StringIO.StringIO('<html><body>Dummy Page</body></html>')
    return res
    
# monkey patching
original_urllib = urllib.urlopen
urllib.urlopen = fakeopen
# test d'exemple
res = urllib.urlopen('http://google.fr')
assert(res.readlines(), ['<html><body>Dummy Page</body></html>'])

# retrait du patch
urllib.urlopen = original_urllib
