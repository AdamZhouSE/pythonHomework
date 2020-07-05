t=int(input())
for ti in range(t):
    s=str.lower(input()).replace(',','').replace(' ','').replace(':','').replace('?','').replace('/','')
    ou=0
    for i in range(len(s)):
        if s[i]==s[-1-i]:
            continue
        else:
            ou=1
            break
    if ou==1:
        print('NO')
        print(s)
    else:
        print('YES')
    #print(s)