n=int(input())
arr=list(input())

arr.sort(reverse=True)

index=0
if arr.count("1")>1:
    for i in range(0,len(arr)-1):
        if arr[i]=="1" and arr[i+1]=="0":
            index=i

result="".join(arr[x] for x in range(index,len(arr)))
print(result,end="")