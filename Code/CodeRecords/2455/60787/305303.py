n=int(input())
num=[int(i) for i in input().split()]
branch=[]
for f in range(0,n):
    branch.append([int(k) for k in input().split()])
print(branch)