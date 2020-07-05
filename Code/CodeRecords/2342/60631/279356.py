t = int(input())
for ti in range(t):
    s=input().split(' ')
    e=int(s[0])
    d=int(s[1])
    li=input().split(' ')
    out = []
    for i in range(len(li)):
        if i%d!=0:
            continue
        for j in reversed(li[i:i+d]):
            out.append(j)
    for i in out:
        print(i,end=' ')
    print()
    