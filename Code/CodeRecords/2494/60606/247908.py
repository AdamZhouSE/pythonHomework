s = input()
array = s[1:len(s)-1].split(",")
array = [int(x) for x in array]
result = 0
for i in range(len(array)-1):
    for j in range(1,len(array)):
        if array[i] > array[j] * 2:
            result += 1
print(result)