n=int(input())
a=map(int,input().split())
b=[4,8,15,16,23,42]
s=[0]*6
for x in a:
    i=b.index(x)
    if i==0:
        s[i]+=1
    if s[i-1]>s[i]:
        s[i]+=1
print(n-s[5]*6)