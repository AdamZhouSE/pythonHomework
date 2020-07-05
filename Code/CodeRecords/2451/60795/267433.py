arr=[int(n) for n in input().split(',')]
target=int(input())
index=-1
for i in range(0,len(arr)):
    if target==arr[i]:
        index=i
        break
    elif target>arr[i]:
        if i+1<len(arr):
            if target<=arr[i+1]:
                index=i+1
                break
            else:
                continue
        else:
            index=len(arr)
            break
    else:
        if i-1<0:
            index=0
            break
        
            
print(index)
