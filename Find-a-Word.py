"""Find a Word."""
import re

N = int(raw_input())

sentences = str()
for _ in xrange(N):
    sentences += raw_input()
    sentences += ' '

T = int(raw_input())

for _ in xrange(T):
    regex = '((?<=[^a-zA-Z0-9_])|(?<=\\b))' + raw_input() + '((?=[^a-zA-Z0-9_])|(?=\\b))'
    print len(re.findall(regex, sentences))
