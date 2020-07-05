def intToBi(x):
    temp=""
    while(x>1):
        temp=str(x%2)+temp
        x=x//2
    temp=str(x)+temp
    return temp

t=eval(input())
for i in range(0,t):
    result=-1
    arr=input().split()
    for j in range(0,len(arr)):
        arr[j]=int(arr[j])
    temp1=intToBi(arr[0])
    temp2=intToBi(arr[1])
    if(len(temp1)>=len(temp2)):
        while(len(temp1)>len(temp2)):
            temp2="0"+temp2
        for k in range(0,len(temp1)):
            if temp1[len(temp1)-1-k]!=temp2[len(temp1)-1-k]:
                result=k+1
                break
    else:
        while(len(temp2)>len(temp1)):
            temp1="0"+temp1
        for k in range(0,len(temp1)):
            if temp1[len(temp1)-1-k]!=temp2[len(temp1)-1-k]:
                result=k+1
                break
    print(result)