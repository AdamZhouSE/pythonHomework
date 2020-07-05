tests = int(input())

lists = []
for i in range(tests):
    temp = list(map(int, input().split()))
    lists.append(temp)
#print(lists)

for i in range(lists.__len__()):
    arr = lists[i]
    result = arr[1] - arr[0] -1
    print(result)
