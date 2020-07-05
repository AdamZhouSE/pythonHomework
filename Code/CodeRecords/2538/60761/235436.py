arr=input("")
arr=list(map(int,arr[1:-1].split(",")))
arr.sort()
i=0
if(arr[0]>=2):
    print(1)
else:
    while(i<len(arr)):
        if(arr[i]>0):
            if(i==len(arr)-1):
                print(arr[i]+1)
                break
            elif(arr[i]+1!=arr[i+1]):
                print(arr[i]+1)
                break
        i=i+1    

