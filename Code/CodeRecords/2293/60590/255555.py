tests = int(input())
lists = []
for i in range(tests):
    arrSize = int(input())
    temp = list(map(int, input().split()))
    lists.append(temp)
    k = int(input())
    lists.append(k)

#print(lists)
res = []
for i in range(0,lists.__len__(),2):
    arr = lists[i]
    k = lists[i+1]
    arr.sort()
    res.append(arr[k-1])
#print(res)

for i in range(res.__len__()):
    print(res[i])