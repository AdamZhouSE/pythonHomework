n=int(input())
l=list(map(int,input().split()))
l.sort()
print(min(l[-2]-l[0],l[-1]-l[1]))