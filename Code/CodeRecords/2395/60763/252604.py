def zeroMove(s):
    for j in range(s.count('0')):
        s.remove('0')
        s.append('0')
    return s

T = int(input())
for i in range(T):
    n = int(input())
    s = ('' + input()).split(' ')
    #print(s)
    count = s.count('0')
    for j in range(len(s)-count):
        if s[j] == s[j+1]:
            s[j+1] = '0'
            s[j] = str(int(s[j])*2)
            s = zeroMove(s)
        # print(s)
    print(' '.join(s))