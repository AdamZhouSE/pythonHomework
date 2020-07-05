N=int(input())
a=[0]*100
for i in range(0,N):
    s=input().split()
    for j in range(0,3):
        s[j]=int(s[j])
    for j in range(s[0],s[1]):
        if a[j]<s[2]:
            a[j]=s[2]
print(sum(a))
