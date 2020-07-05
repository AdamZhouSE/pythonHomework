n = int(input())

xlist = input().split()
serviceTime = [int(xlist[i]) for i in range(n)]

count = 1
serviceTime.sort()
for i in range(1, n):
    if sum(serviceTime[:i]) <= serviceTime[i]:
        count +=1

print(count)



