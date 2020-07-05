from functools import reduce
tests = int(input())

lists = []
for i in range(tests):
    size = int(input())
    temp = list(map(int, input().split()))
    lists.append(temp)
#print(lists)

res = []
for i in range(lists.__len__()):
    temp = []
    arr = lists[i]
    mul = reduce(lambda x,y: x*y, arr)
    for j in range(arr.__len__()):
        n = int(mul/arr[j])
        temp.append(n)
    res.append(temp)
#print(res)

for i in range(res.__len__()):
    if i!=0:
        print()
    for j in range(res[i].__len__()):
        if j == res[i].__len__()-1:
            print(res[i][j], end="")
        print(res[i][j], end=" ")