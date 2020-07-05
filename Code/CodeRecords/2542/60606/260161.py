array = input()[1:-1].split(", ")
array = [int(x) for x in array]
array.sort()
length = 1
Max = 0
for i in range(len(array)-1):
    if array[i] - array[i+1] == -1:
        length += 1
    else:
        Max = max(length,Max)
        length = 1
print(Max)
