lists = list(map(int, input().split(",")))
target = int(input())

res = []
start = 0
end = 0

flag = False
for i in range(lists.__len__()):
    if lists[i] == target:
        start = i
        flag = True
        break
for i in range(lists.__len__()):
    if lists[lists.__len__()-1-i] == target:
        end = lists.__len__()-1-i
        flag = True
        break

#print(start)
#print(end)
res.append(start)
res.append(end)
#print(res)

if flag:
    print(res)
else:
    print([-1,-1])
