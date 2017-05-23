N = int(raw_input())

for _ in xrange(N):
    text = raw_input()
    if 'hackerrank' in text:
        if len(text.split()) == 1:
            print 0
        elif (text.split()[-1] == 'hackerrank'):
            print 2
        elif (text.split()[0] == 'hackerrank'):
            print 1
        else:
            print -1
    else:
        print -1
