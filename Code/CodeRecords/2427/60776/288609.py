a=int(input())
for k in range(0,a):
    a=input()
    b = input().split(' ')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    c=[]
    result=len(b)
    for i in range(0,len(b)):
        if b[i] in c:
            for j in range(0,len(c)):
                if c[j]==b[i]:
                    if j<result:
                        result=j
                    break
        else:
            c.append(b[i])
    if result==len(b):
        print(-1)
    else:
        print(result+1)