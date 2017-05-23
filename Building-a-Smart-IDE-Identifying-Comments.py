import re
import sys

text = sys.stdin.read()
regex = r'//.+|/\*\*[\w\s]*\*\*/|/\*[^"]*?\*/'

matches = re.findall(regex, text)

for match in matches:
    match = re.sub(r'\n\s+', '\n', match)  # modification for Test Case #4
    print match
