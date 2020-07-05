n=int(input())
for a in range(0,n):
    num=int(input())
    arr=input().split(" ")
    arr=list(int(a) for a in arr)
    res=""
    i=0
    while(i<(num-1)//2):
        res=res+str(arr[num-1-i])+" "+str(arr[i])+" "
        i=i+1
    if(num%2==1):
        res=res+str(arr[i])
    else:
        res=res+str(arr[num-1-i])+" "+str(arr[i])
    print(res,end=" \n")
    
