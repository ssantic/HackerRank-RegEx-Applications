"""Detect HTML Attributes."""
import re
import collections

dic = {}
list1, list2, list3 = [],[],[]

N = int(raw_input())

for _ in range(N):
    x = raw_input()
    list1.extend(re.findall(r'<(\w+)>', x))
    list2.extend(re.findall(r'<\w+\s.+?>', x))

for var in list2:
    list3.extend(re.findall(r'<(\w+)\s(\w+)=(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?(?:.+?\s(\w+)=)?',var))

for var in list3:
    if var[0] in dic.keys():
        dic[var[0]].extend(list(filter(None, var[1:])))
    else:
        dic[var[0]] = list(filter(None, var[1:]))

for var in list1:
    dic[var] = ''

for key, value in (collections.OrderedDict(sorted(dic.items(), key=lambda dic: dic[0]))).iteritems():
    print "%s:%s" % (key, ','.join(sorted(list(set(value)))))
