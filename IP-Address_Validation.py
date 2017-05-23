import re

ip4 = r'^((1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.){3}(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$'
ip6 = r'^([0-9a-f]+:){7}[0-9a-f]+$'

for N in xrange(int(raw_input())):
    text = raw_input()
    if re.search(ip4, text):
        print 'IPv4'
    elif re.search(ip6, text):
        print 'IPv6'
    else:
        print 'Neither'
