num=int(input())
for i in range(num):
    length=int(input())
    temp=input().split()
    array=[[] for _ in range(length)]
    for j in range(length):
        array[j]=list(temp[j])
        array[j].sort()
    array.sort()
    result=[]
    count=1
    for j in range(length-1):
        if array[j]==array[j+1]:
            count=count+1
        else:
            result.append(str(count))
            count=1
    result.append(str(count))
    result.sort()
    print(' '.join(result))