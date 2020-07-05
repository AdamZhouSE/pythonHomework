def move_stone():
    arr=list(map(int,input().split(',')))
    arr.sort()
    length=len(arr)
    if length<=2:
        return [0,0]
    d1=arr[1]-arr[0]-1
    d2=arr[-1]-arr[-2]-1
    if d1==d2==0:
        return [0,0]
    if d1!=0 and d2!=0:
        return [min(d1,d2),max(d1,d2)]
    d=d1+d2
    return [min(2,d),d]
    
print(move_stone())