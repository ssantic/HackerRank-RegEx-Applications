import re

N = int(raw_input())

regex = r"[(][-+]?(([0-8]?\d(\.\d+)?)|(90(\.0+)?)), [-+]?(((\d|1[0-7])\d(\.\d+)?)|(180(\.0+)?))[)]"

for _ in xrange(N):
    text = raw_input()
    if re.search(regex, text):
        coordinates = text.lstrip('(').rstrip(')').split(',')
        latitude, longitude = float(coordinates[0]), float(coordinates[1])
        if (-90 <= latitude <= 90) and (-180 <= longitude <= 180):
            print 'Valid'
        else:
            print 'Invalid'
    else:
        print 'Invalid'
