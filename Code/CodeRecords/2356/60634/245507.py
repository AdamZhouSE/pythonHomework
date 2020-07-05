problems = int(input())
for x in range(problems):
    size = int(input())
    array = input().split(" ")
    
    if size <= 2:
        print(-1)
    else:
        model = False 
          # False :find the middle number
          # True  :make sure latter number bigger than the middle
        middle = 0
        i = 1
        array[0] = int(array[0])
        while i < size:
            array[i] = int(array[i])
            if model:
                if array[i] < array[middle]:
                    model = False
            else:
                if array[i] >= array[middle]:
                    middle = i
                    model = True
            i += 1
        if middle==0 or middle==size-1 or not model:
            print(-1)
        else:
            print(array[middle])