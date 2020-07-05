arrange = input().split(" ")
arr = []
all = input().split(" ")
for i in range(len(all)):
    all[i] = int(all[i])
for i in range(int(arrange[1])):
    arr.append(input().split(" "))
n = int(input())
for i in range(len(arr)):
    left = all[:int(arr[i][1])-1]
    temp = all[int(arr[i][1])-1:int(arr[i][2])]
    right = all[int(arr[i][2]):]
    if arr[i][0] == "0":
        temp.sort()
    else:
        temp.sort(reverse=True)
    all = left+temp+right
print(all[n-1])