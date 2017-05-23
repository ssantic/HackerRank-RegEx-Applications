import re

regex = r"[A-Z]{5}\d{4}[A-Z]"

N = int(raw_input())

for _ in xrange(N):
    text = raw_input()
    if re.match(regex, text):
        print 'YES'
    else:
        print 'NO'
