tests = int(input())
for t in range(tests):
    n=int(input())
    array=[int(x) for x in input().split()]
    evens=[]
    index=0
    while index<len(array):
        tmp=array[index]
        if tmp%2==0:
            array.remove(tmp)
            evens.append(tmp)
        else:
            index+=1
    evens.extend(array)
    print(*evens,end=' \n')