def count(array,trap):
    if array[trap]==-1:
        return 0
    num=1
    i=trap+1
    while i<len(array) and array[i]==0:
        i=i+1
        num=num+1
    i=trap-1
    while i>-1 and array[i]==0:
        i=i-1
        num=num+1
    return num
number=input().split()
array=[0]*int(number[0])
last_destroy=[]
for i in range(int(number[1])):
    temp=input().split()
    if temp[0]=='D':
        array[int(temp[1])-1]=-1
        last_destroy.append(int(temp[1])-1)
    elif temp[0]=='R':
        if len(last_destroy)!=0:
            replace=last_destroy.pop()
            array[replace]=0
    else:
        trap=int(temp[1])-1
        print(count(array,trap))