"""Detecting email addresses."""
import re

regex = r"[a-zA-Z_.-0-9+]+@[a-zA-Z0-9.]+[a-zA-Z]+"

text = str()
N = int(raw_input())

for _ in xrange(N):
    text += raw_input()
    text += ' '

addresses = sorted(set(re.findall(regex, text)))

output = str()
for address in addresses:
    output += address
    output += ';'

print output.rstrip(';')
