T=int(input())
for a in range(0,T):
    strin=input()
    arr=[1]
    i=1
    maxLen=arr[0]
    while(i<len(strin)):
        temp=[]
        j=0
        sig=True
        while(j<len(arr)):
            if(strin[j]<strin[i]):
                temp.append(arr[j])
                sig=False
            j=j+1
        if sig:
            arr.append(1)
        else:
            arr.append(max(temp)+1)
            if max(temp)+1>maxLen:
                maxLen=max(temp)+1
        i=i+1
    print(maxLen)