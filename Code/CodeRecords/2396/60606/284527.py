def reverse(array,start,end):
    temp = array[start:end].copy()
    temp.reverse()
    temp =array[0:start]+temp
    temp += array[end:]
    return temp
n = int(input())
array = input().split(" ")
array = [int(x) for x in array]
origin = array.copy()
origin.sort()
for i in range(len(array)):
    temp = origin[i]
    for j in range(len(array)):
        if array[j] == temp and i!=j:
            index = j
            array = reverse(array,i,index+1)
            print(index+1,end=" ")
            break
print(array.index(origin[n-1])+1,end=" ")
