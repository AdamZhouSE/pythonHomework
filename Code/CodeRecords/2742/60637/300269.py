import copy
n=(int)(input())
operations=[]
versions=[]
def operation(arr,opt,x):
    if(opt==1):
        arr.append(x)
        return sorted(arr)
    elif(opt==2):
        del arr[arr.index(x)]
        return arr
    elif(opt==3):
        return arr.index(x)+1
    elif(opt==4):
        rate=0
        record=[]
        for i in arr:
            if(i not in record):
                record.append(i)
                rate+=1
            if(rate==x):
                return record[-1]
    elif(opt==5):
        for i in range(0,len(arr)):
            if(arr[i]>=x):
                if(i==0):
                    return -pow(2, 31)+ 1
                else:
                    return arr[i-1]
        return arr[-1]
    elif(opt==6):
        for i in range(0, len(arr)):
            if(arr[i]>x):
                return arr[i]
        return pow(2, 31)
for i in range(n):
    operations.append(list(map(int,input().split(' '))))
for i in operations:
    if(i[0]==0):
        temp=operation([],i[1],i[2])
    else:
        temp=operation(copy.deepcopy(versions[i[0]-1]),i[1],i[2])
    if(i[1]==1 or i[1]==2):
        versions.append(temp)
    else:
        versions.append(copy.deepcopy(versions[i[0]-1]))
        print(temp)
