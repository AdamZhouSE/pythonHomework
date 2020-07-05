n=int(input())
l=[]
for i in range(n):
    l+=list(map(int,input().split(',')))
l=sorted(l)
print(l[int(input())-1])