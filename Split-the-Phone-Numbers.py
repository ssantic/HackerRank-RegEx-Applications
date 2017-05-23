import re

regex = r"(\d+)[ -](\d+)[ -](\d+)"

N = int(raw_input())

for _ in xrange(N):
    phone = raw_input()
    if re.search(regex, phone):
        country = re.search(regex, phone).group(1)
        area = re.search(regex, phone).group(2)
        number = re.search(regex, phone).group(3)
        print 'CountryCode=%s,LocalAreaCode=%s,Number=%s' % (country, area, number)
