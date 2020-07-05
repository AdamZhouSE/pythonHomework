n=eval(input())
if n==1:
    print("[-1]")
else:
    arr=[]
    for i in range(0,n):
        temp1=input().split(',')
        temp1[0]=int(temp1[0])
        temp1[1]=int(temp1[1])
        arr.append(temp1)
    result=[]
    index=-1
    flag=0
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                continue
            else:
                if arr[j][0]>=arr[i][1]:
                    if flag==0:
                        temp2=arr[j][0]
                        index=j
                    else:
                        if arr[j][0]<temp2:
                            temp2=arr[j][0]
                            index=j
        result.append(index)
        index=-1
    print(result)
