array = input().split(",")
array = [int(x) for x in array]
array.sort()
sentinel = -1
for i in range(len(array)-1):
    if array[i] == array[i+1]:
        sentinel = array[i]
        break
print(sentinel)