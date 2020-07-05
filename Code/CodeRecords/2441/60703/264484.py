def mergeSort(array,tempArray,left,right):
    if(left<right):
        center = (left+right)//2
        mergeSort(array,tempArray,left,center)
        mergeSort(array,tempArray,center+1,right)
        merge(array,tempArray,left,center+1,right)


def merge(array , tempArray:list,leftPos,rightPos,rightEnd):
    leftEnd = rightPos-1
    tempPos = leftPos
    numElements = rightEnd-leftPos+1
    while leftPos<=leftEnd and rightPos<=rightEnd:
        if array[leftPos]<=array[rightPos]:
            tempArray[tempPos] = array[leftPos]
            tempPos+=1
            leftPos+=1
        else:
            tempArray[tempPos] = array[rightPos]
            # tempArray.append(array[rightPos])
            rightPos+=1
            tempPos+=1
    while rightPos<=rightEnd:
        tempArray[tempPos] = array[rightPos]
        rightPos+=1
        tempPos+=1
    while leftPos<=leftEnd:
        tempArray[tempPos] = array[leftPos]
        leftPos+=1
        tempPos+=1
    for i in range(numElements):
        array[rightEnd] = tempArray[rightEnd]
        rightEnd-=1
#
# array = [4,2,1,3]

# tempArr = [0,0,0,0]
# mergeSort(array,tempArr,0,3)
# print(tempArr)
# print(array)
array = eval(input())
length = len(array)
temp = []
for i in range(length):
    temp.append(0)
mergeSort(array,temp,0,length-1)
print(array)