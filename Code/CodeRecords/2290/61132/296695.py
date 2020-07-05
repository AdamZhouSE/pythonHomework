n=int(input())
for i in range(n):
    m=input()
    l=list(map(int,input().split()))
    l.append(l[-1]+1)
    ans=[l[i+1] if l[i+1]<l[i] else -1 for i in range(len(l)-1)]