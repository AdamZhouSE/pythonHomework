tests =int(input())
lists = []
for i in range(tests):
    temp = list(map(int, input().split()))
    lists.append(temp)

result = []
for i in range(lists.__len__()):
    n = lists[i][0] * lists[i][1]
    result.append(n)

for i in range(result.__len__()):
    print(result[i])