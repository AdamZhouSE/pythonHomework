n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
arr_reverse=arr[::-1]
counter=0
for i in range(0,len(arr)):
    if(arr[i]>k):
        break
    else:
        counter+=1

if(counter==len(arr)):
    print(counter)
else:
    for i in range(0,len(arr_reverse)):
        if(arr_reverse[i]>k):
            break
        else:
            counter+=1
    print(counter)
