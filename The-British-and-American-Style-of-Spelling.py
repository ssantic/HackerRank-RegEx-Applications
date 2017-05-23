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
    regex = test[:-2] + "[s|z]e(?!\w)"
    results.append(len(re.findall(regex, sentences)))

for result in results:
    print result
