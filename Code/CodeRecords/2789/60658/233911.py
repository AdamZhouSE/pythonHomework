k = int(input())
for i in range(k):
    n = int(input())
    li = [int(x) for x in input().split()]
    li.sort(reverse=True)
    temp = 0
    for index,k in enumerate(li,start=1):
        temp = max(min(index,k),temp)
    print(temp)