problems = int(input())
for x in range(problems):
    size = int(input())
    array = input().split(" ")
    d = int(input())
    
    temp = array[0:d]
    i = d
    while i < size:
        array[i-d] = array[i]
        i += 1
    i = 0
    while i < d:
        array[size-d+i] = temp[i]
        i += 1
    for n in array:
        print(n,end=" ")
    print()