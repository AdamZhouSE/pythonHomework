s = int(input())
lists = list(map(int, input().split(",")))

#temp = []
res = []
for i in range(1, lists.__len__()+1):
    for j in range(lists.__len__()+1-i):
        arr = lists[j:j+i]
        #temp.append(arr)
        total = sum(arr)
        if total >= s:
            res.append(i)
#print(temp)
print(min(res))