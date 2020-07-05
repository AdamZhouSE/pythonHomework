problems = int(input())
for p in range(problems):
    size = int(input())
    array = input().split(" ")
    
    count = 0
    
    if size < 3:
        print(-1)
    else:
        array[0] = int(array[0])
        array[1] = int(array[1])
        i = 0
        while i < size-2:
            j = i + 1
            while j < size-1:
                k = j + 1
                while k < size:
                    array[k] = int(array[k])    
                    if (array[i]+array[j]==array[k])or(array[i]+array[k]==array[j])or(array[k]+array[j]==array[i]):
                        count += 1
                
                    k += 1
                j += 1
            i += 1
        if count == 0:
            print(-1)
        else:
            print(count)