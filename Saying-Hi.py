import re

regex = r"^[hH][iI]\s[^dD]"

N = int(raw_input())

for _ in xrange(N):
    sentence = raw_input()
    if re.search(regex, sentence):
        print sentence
