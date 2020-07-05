numlist=list(map(int,input().split(",")))
k=int(input())
numlist.sort()
print(numlist[-k])