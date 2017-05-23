import re

N = int(raw_input())
regex = r"[hH][aA][cC][kK][eE][rR][rR][aA][nN][kK]"

result = 0
for _ in xrange(N):
    text = raw_input()
    if len(re.findall(regex, text)) > 0:
        result += len(re.findall(regex, text))

print result
