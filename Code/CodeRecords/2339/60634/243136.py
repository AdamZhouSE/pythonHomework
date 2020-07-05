problems = int(input())
for x in range(problems):
    size = int(input())
    array = input().split(" ")
    
    count = 0
    i = 0
    while i < size - 1:
        j = i + 1
        while j < size:
            if array[j] < array[i]:
                count += 1
            j += 1
        i += 1
    print(count)