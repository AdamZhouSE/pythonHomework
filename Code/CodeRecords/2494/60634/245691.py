array = eval(input())
count = 0
i = 0
while i < len(array)-1:
    j = i + 1
    while j < len(array):
        if array[i] > 2*array[j]:
            count += 1
        j += 1
    i += 1
print(count)