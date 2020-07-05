arr=eval(input())
def get_min_max(arr,start,end):
    Min=arr[start]
    Max=arr[start]
    for i in range(start+1,end):
        Max=max(Max,arr[i])
        Min=min(Min,arr[i])
    return Min,Max
length=len(arr)
start=0
end=length
while length>1:
    Min,Max=get_min_max(arr,start,end)
    if arr[start]==Min or arr[end-1]==Max:
        if arr[start]==Min:
            length-=1
            start+=1
        if arr[end-1]==Max:
            length-=1
            end-=1
    else:
        print(length)
        break
if length==1:
    print(0)

