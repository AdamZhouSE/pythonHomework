def count(array):
    list=[]
    for i in range(len(array)):
        total=0
        j=i
        while j<len(array) and array[j]!=-1:
            total=total+array[j]
            j=j+1
        list.append(total)
    return max(list)
number=int(input())
array=input().split()
for i in range(number):
    array[i]=int(array[i])
cycle=input().split()
for i in range(len(cycle)):
    cycle[i]=[int(cycle[i]),i]
cycle.sort()
for i in range(len(cycle)):
    num=cycle[i][1]
    array[num]=-1
    if count(array)==18 :
        print(array)
        print(cycle)
    print(count(array))