arr = list(input())
#print(arr)

lists = []
index1 = 0
index2 = 0
for i in range(arr.__len__()):
    if arr[i] == '[':
        index1 = i+1
    if arr[i] == ']':
        index2 = i
#print(index1)
#print(index2)
for i in range(index1, index2, 2):
    lists.append(arr[i])
#print(lists)

indexK = 0
indexT = 0
for i in range(arr.__len__()):
    if arr[i] == 'k':
        indexK = i
    if arr[i] == 't':
        indexT = i

startOfk = indexK + 4
k = arr[startOfk]
while arr[startOfk+1] != ',':
    startOfk = startOfk+1
    k = k+arr[startOfk]
k = int(k)
#print(k)

t = ""
startOft = indexT + 4
for i in range(startOft, arr.__len__()):
    t = t+arr[i]
t = int(t)
#print(t)


res = "false"
for i in range(lists.__len__()):
    index1 = i
    index2 = i+k
    if index1 < lists.__len__() and index2 < lists.__len__():
        if int(lists[index2]) - int(lists[index1]) == t:
            res = "true"

print(res)