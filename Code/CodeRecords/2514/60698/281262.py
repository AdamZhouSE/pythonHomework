def test():
    s=input()
    t=input()
    if len(s)>len(t):
        print('False')
        return
    j=0
    count=0
    for i in range(0,len(s)):
        for k in range(j,len(t)):
            if s[i]==t[k]:
                count=count+1
                j=k+1
                break
    if count==len(s):
        print('True')
    else:
        print('False')

test()
