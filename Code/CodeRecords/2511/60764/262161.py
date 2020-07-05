n,s=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
for i in range(n):
    j=1
    while i+2*j<=n:
        if sum(l[i:i+j])<=s and sum(l[i+j:2*j+i])<=s:
            j+=1
        else:
            break
    print((j-1)*2)