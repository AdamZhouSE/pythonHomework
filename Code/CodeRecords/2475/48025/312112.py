t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    max=0
    for j in range(0,len(arr)):
        counter=1
        while(True):
            if arr[j]+counter in arr:
                counter+=1
            else:
                break
        if(max<counter):
            max=counter
    print(max)