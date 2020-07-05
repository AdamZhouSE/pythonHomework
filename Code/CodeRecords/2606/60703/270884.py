def BinarySerach(array:list,target:int):
    start = 0
    end = len(array)-1
    middle = 0
    while start<=end:
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
            end = numMiddle
        elif numMiddle<target:
            start = numMiddle
    return "-1"

List = eval(input())
target = int(input())
res = str(BinarySerach(List,target))
if(res ==""):
    print(List)
    print(target)


print(BinarySerach(List,target))