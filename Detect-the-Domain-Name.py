# Enter your code here. Read input from STDIN. Print output to STDOUT
"""Detecting domain names from HTML."""
import re

regex = r'[=\'\"](?:https{0,1}\:\/\/(?:ww[w0-9]\.){0,1})([0-9a-zA-Z][0-9a-zA-Z_\-\.]+\.[a-zA-Z]+)'

N = int(raw_input())

html = str()
for _ in xrange(N):
    html += raw_input()
    html += ' '

matches = re.findall(regex, html)

results = sorted(set(matches))

output = str()
for result in results:
    output += result
    output += ';'

print output.rstrip(';')
