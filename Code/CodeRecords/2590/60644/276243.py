t=int(input())
for i in range(0,t):
    s=input()
    a=list(s)
    if a.count('a')>0:
        for j in range(0,a.count('a')):
            a.remove('a')
    if a.count('e') > 0:
        for j in range(0, a.count('e')):
            a.remove('e')
    if a.count('i') > 0:
        for j in range(0, a.count('i')):
            a.remove('i')
    if a.count('o') > 0:
        for j in range(0, a.count('o')):
            a.remove('o')
    if a.count('u') > 0:
        for j in range(0, a.count('u')):
            a.remove('u')
    c=set(a)
    if len(c)%2==1:
        print('HE!')
    else:
        print('SHE!')
