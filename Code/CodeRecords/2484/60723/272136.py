num=int(input())
for i in range(num):
    count=0
    temp=input().split()
    N=int(temp[0])
    M=int(temp[1])
    array1=input().split()
    array2=input().split()
    for j in range(len(array1)-1,-1,-1):
        if array2.count(array1[j])!=0:
            count=count+1
        if array1.count(array1[j])>1:
            array1.pop(j)
    for j in range(len(array2)-1,-1,-1):
        if array2.count(array1[j])>1:
            array2.pop(j)
    if len(array1)+len(array2)-count==3:
        print(' '.join(temp)+'\n'+' '.join(array1)+'\n'+' '.join(array2))
    else:
        print(len(array1)+len(array2)-count)