array = input().split(",")
array = [int(x) for x in array]
target = int(input())
result = []
sentinel = 0
for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if array[i] + array[j] == target:
            result.append(i+1)
            result.append(j+1)
            sentinel = 1
            break
    if sentinel == 1:
        break
if sentinel == 0:
    print("None")
else:
    print(result)