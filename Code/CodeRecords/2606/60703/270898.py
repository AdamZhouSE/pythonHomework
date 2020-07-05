def BinarySerach(array:list,target:int):
    start = 0
    end = len(array)-1
    middle = 0
    numStart = 0
    numEnd = 0
    numMiddle = 0
    while start<end:
        if(middle-start==1 or end-middle==1):
            break
        middle = ((end + start) // 2)
        numStart = array[start]
        numEnd = array[end]
        numMiddle = array[middle]
        if(numStart==target):
            return start
        if(numEnd == target):
            return end
        if(numMiddle==target):
            return middle
        if(numMiddle>target):
            end = middle
        elif numMiddle<target:
            start = middle
    if (numStart == target):
        return start
    if (numEnd == target):
        return end
    if (numMiddle == target):
        return middle
    return "-1"

List = eval(input())
target = int(input())
res = str(BinarySerach(List,target))
if(res ==""):
    print(List)
    print(target)


print(BinarySerach(List,target))