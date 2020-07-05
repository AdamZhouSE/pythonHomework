n=int(input())
d=[int(i) for i in input().split()]
a,b=map(int,input().split())
sum=0
for i in range(a-1,b-1):
    sum+=d[i]
print(str(sum))