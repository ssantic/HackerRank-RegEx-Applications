import re

regex = r"^(_|\.)([0-9]+[a-zA-Z]*_?)$"

N = raw_input()
for _ in xrange(int(raw_input())):
    if re.search(regex, raw_input()):
        print 'VALID'
    else:
        print 'INVALID'
