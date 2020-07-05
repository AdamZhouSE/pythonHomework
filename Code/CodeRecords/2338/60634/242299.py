problems = int(input())
for x in range(problems):
    temp = input().split(" ")
    size = int(temp[0])
    X = int(temp[1])
    
    array = input().split(" ")
    for x in range(size):
        array[x] = int(array[x])
    array.append(X)
    
    result = "No"
    
    i = 0
    flag = True
    while (i < len(array) - 1)and flag:
        j = i + 1
        while j < len(array):
            if array[i] + array[j] == X:
                result = "Yes"
                flag = False
                break
            j += 1
        i += 1
        
    print(result)