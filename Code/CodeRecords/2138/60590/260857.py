lists = list(map(int, input().split(",")))
k = int(input())

arr =[ ]
for subArrlen in range(2, lists.__len__()+1):
    for i in range(lists.__len__()-subArrlen+1):
        temp = lists[i:i+subArrlen]
        arr.append(sum(temp))
#print(arr)

flag = False
for i in range(arr.__len__()):
    if i % k == 0:
        flag = True

print(flag)