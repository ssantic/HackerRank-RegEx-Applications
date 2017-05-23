import re

regex = r"[a-z]{0,3}\d{2,8}[A-Z]{3,}"

N = int(raw_input())

for _ in xrange(N):
    text = raw_input()
    if re.match(regex, text):
        print 'VALID'
    else:
        print 'INVALID'
