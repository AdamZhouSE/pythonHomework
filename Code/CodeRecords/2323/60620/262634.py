a=list(map(int,input().split(',')))
k=int(input())
print(max(0,max(a)-min(a)-2*k))