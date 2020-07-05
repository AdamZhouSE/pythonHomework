N = int(input())
A = input().split(' ')
F = input().split(' ')
listA=[]
listB=[]
for x in A:
    listA.append(int(x))
for y in F:
    listB.append(int(y))
sum = 0
visited=[]
for x in range(0, N):
    while not visited.__contains__(x):
        sum=sum+listA[x]
        visited.append(x)
        x=listB[x]-1
    print(sum)
    sum=0
    visited.clear()




