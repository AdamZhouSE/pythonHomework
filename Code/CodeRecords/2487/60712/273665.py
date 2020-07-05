from collections import Counter

n = int(input())
for i in range(n):
    x=input()
    sorstr= input().split()
    c = Counter(sorstr)
    b=list(c.items())
    output=sorted(b,key=lambda s:s[1])
    print(output[len(output)-1][0],output[len(output)-1][1])
