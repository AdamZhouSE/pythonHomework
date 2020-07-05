s = input()
array = s[1:len(s)-1].split(",")
array = [int(x) for x in array]
odd = []
even = []
result = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        even.append(array[i])
    else:
        odd.append(array[i])
for i in range(len(odd)):
    result.append(even[i])
    result.append(odd[i])
print(result)
        