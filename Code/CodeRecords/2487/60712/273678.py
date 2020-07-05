from collections import Counter

n = int(input())
for i in range(n):
    x=input()
    sorstr= input().split()
    c = Counter(sorstr)
    b=list(c.items())
    output=sorted(b,key=lambda s:(s[0],-s[1]))
    print(output[0][0],output[0][1])
