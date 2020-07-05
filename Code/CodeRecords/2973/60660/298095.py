import collections
s=input()
n=int(input())
sum=0
for _ in range(n):
    c1=collections.Counter(input())
    for i in range(0,len(s)-7):
        c2=collections.Counter(s[i:i+8])
        if c1==c2:
            sum+=1
print(sum)