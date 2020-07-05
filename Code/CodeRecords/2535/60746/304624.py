def arrsum(arr,s,t):
    sum=0
    for i in range(s,t):
        sum=sum+arr[i]
    return sum

def nsum(s,t):
    sum=(s+t)*(t-s+1)/2
    return sum

def chunksnum(arr:list):
    n=len(arr)
    result=0
    t=1
    s=1
    for k in range(0,n):
        i=t
        for j in range(i,n):
            if arrsum(arr,0,j+1)==nsum(0,j):
                s=1
                pass
            elif s==1:
                s=0
                result=result+1
                t=j+1
            else:
                t=t+1
    return result

arr=[4,3,2,1,0]
print(chunksnum(arr))
