"""Parsing words with British or American spelling."""
import re

N = int(raw_input())
sentences = str()
for _ in xrange(N):
    sentences += raw_input()
    sentences += ' '

T = int(raw_input())
tests = list()
for _ in xrange(T):
    tests.append(raw_input())

results = list()
for test in tests:
    if 'our' in test:
        regex = '\\b' + test.replace('our', '(ou?r)') + '\\b'
    else:
        regex = '\\b' + test.replace('or', '(ou?r)') + '\\b'
    results.append(len(re.findall(regex, sentences)))

for result in results:
    print result
