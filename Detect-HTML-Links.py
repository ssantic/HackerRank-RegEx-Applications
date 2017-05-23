"""Detecting HTML links and names."""
import re

regex = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'

N = int(raw_input())

for _ in xrange(N):
    text = raw_input()
    result = re.findall(regex, text)
    for link, title in result:
        print '%s,%s' % (link, title.strip())
