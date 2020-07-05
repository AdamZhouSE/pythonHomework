T = int(input())
for i in range(T):
    n = int(input())
    s = ('' + input()).split(' ')
    # s = list(map(int, s))
    for j in range(s.count('0')):
        s.remove('0')
        s.append('0')
    print(' '.join(s)+' ')