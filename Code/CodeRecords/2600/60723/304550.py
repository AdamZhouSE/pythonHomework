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
    cycle[i]=int(cycle[i])-1
for i in range(len(cycle)):
    num=cycle[i]
    array[num]=-1
    print(str(count(array)))