def overArray(fr,to,array):
    while fr < to:
        temp = array[fr]
        array[fr] = array[to]
        array[to] = temp
        fr += 1
        to -= 1
        

problems = int(input())
j = 0 
while j < problems:
    temp = input().split(" ")
    size = int(temp[0])
    k = int(temp[1])
    array = input().split(" ")
    i = 0
    while i < size:
        if i + k > size:
            overArray(i,size-1,array)
        else:
            overArray(i,i+k-1,array)
        i += k

    i = 0
    while i < size:
        print(array[i],end=" ")
        i += 1
    j += 1
    #if j < problems:
    print()