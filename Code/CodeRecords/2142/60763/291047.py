def com(s):
    a = []
    temp = 1
    k = 1
    max1 = 1
    for j in range(len(s)):
        if s[j] == '(':
            b = '' + s[0:j]
            k = b.count('(')+1
            # if b.count('(') - b.count(')') <=1:
            #     k = max1
            # if b.count('(') - b.count(')') == 1:
            #     k  = 1
            # else:
            #     k = max1
            a.append(k)
            k += 1
            # max1 = max(k,max1)
        else:
            b = '' + s[0:j]
            a.append(b.count('(')-b.count(')'))
            # x = b.rfind('(')
            # c = '' + s[x:j]
            # a.append(-c.count(')') + a[x])
            # k -= 1
            # if b.count('(') - b.count(')') == 1 and b[len(b)-1] != '(' and j == len(s)-1:
            #     a.append(1)
            # else:
            #     x = b.rfind('(')
            #     c = '' + s[x:j]
            #     a.append(-c.count(')') + a[x])
            #     k -= 1
    return a



T = int(input())
for i in range(T):
    s1 = "()"
    s2 = ''+input()
    s = ''
    for j in range(len(s2)):
        if s2[j] in s1:
            s = s+s2[j]
    # print(com(s))
    a = com(s)
    for j in range(len(a)-1):
        print(a[j],end=' ')
    print(a[len(a)-1])