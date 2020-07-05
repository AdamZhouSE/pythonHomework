num=int(input())
for i in range(num):
    N=int(input())
    temp=input().split()
    array=[]
    for j in range(N):
        if int(temp[j])>0:
            array.append(int(temp[j]))
    result=0
    array.sort()
    for j in range(len(array)):
        if array[j]>j+1:
            result=j+1
            break
    if result==0:
        result=len(array)+1
    print(result)