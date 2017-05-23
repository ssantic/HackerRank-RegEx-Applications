import re

N = int(raw_input())
text = "\n".join(raw_input() for _ in xrange(N))

T = int(raw_input())
for _ in xrange(T):
    print len(re.findall(r"(?<=\w)%s(?=\w)" % raw_input().strip(), text))
