n=int(input())
l=list(map(int,input().split()))
minpos=l.index(1)
maxpos=l.index(n)
a=min(minpos,maxpos)
b=max(minpos,maxpos)
print(max(a,len(l)-b)+(b-a))