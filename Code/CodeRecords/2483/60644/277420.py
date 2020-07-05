t=int(input())
for i in range(0,t):
    s=input()
    patt=input()
    p=False
    for i in range(0,len(s)):
        if patt.count(s[i:i+1])>0:
            p=True
            print(s[i:i+1])
            break
    if not p:
        print('$')
