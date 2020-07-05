nums=int(input())
arr=list(map(int,input().split(" ")))
count=0
i=1
while i<nums-1:
    if arr[i]==0:
        if arr[i-1]==0 or arr[i+1]==0:
            i+=1
        else:
            if i<nums-2 and arr[i+2]==0:
                count+=1
            else:
                arr[i+1]=1
                count+=1
            i += 3
    else:
        i+=1
print(count)