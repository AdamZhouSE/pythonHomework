s=int(input())
numbers=input().split()
numbers=[int(x) for x in numbers]
rank=input().split()
rank=[int(y) for y in rank]
res=0
for k in range(rank[0]-1,rank[1]-1):
    res=res+numbers[k]
print(res)