N=int(input())
s=[]
n=N
while N>0:
    s.append(input())
    N-=1
else:
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if sorted(s[i])==sorted(s[j]):
                n-=1
    if n==0:
        n=1
    print(n,end='')