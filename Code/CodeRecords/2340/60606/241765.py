def findPool(list, startPos):
    temp = list[startPos]
    for i in range(startPos+1,len(list)):
        if(list[i] >=temp):
            return i
    return len(list)-1

def calPool(list,startPos,end):
    top = min(list[startPos],list[end])
    sum = 0
    for i in range(startPos+1,endPos):
        sum += top-list[i]
    return sum

test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    result = 0
    endPos = findPool(array, 0)
    result += calPool(array,0,endPos)
    while endPos != len(array)-1:
        start = endPos
        endPos = findPool(array,endPos)
        result += calPool(array,start,endPos)
    print(result)