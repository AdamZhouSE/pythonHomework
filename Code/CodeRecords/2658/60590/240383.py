tests = int(input())

lists = []
for i in range(tests):
    temp1 = list(map(int, input().split()))
    temp2 = list(map(int, input().split()))
    lists.append(temp1)
    lists.append(temp2)

#print(lists)
result = []
for i in range(int(lists.__len__()/2)):
    base = lists[2*i][1]
    temparr = []
    for j in range(lists[2*i+1].__len__()):
        num = lists[2*i+1][j]
        if num % base==0:
            temparr.append(num)
    result.append(temparr)

#print(result)

for i in range(result.__len__()):
    if result[i].__len__()==1:
        print(result[i][0])
    elif result[i] == []:
        print(0)
    else:
        ans = result[i][0]
        for j in range(1,result[i].__len__()):
            ans = ans | result[i][j]
        print(ans)