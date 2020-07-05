def test():
    a=input()
    k=int(input())
    arr=a.split(',')
    arr=list(map(int,arr))
    for i in range(0,len(arr)-1):
        sum=arr[i]
        for j in range(i+1,len(arr)):
            sum=sum+arr[j]
            if sum%k==0:
                return True
    return False
                
print(test())   