def find(sum1,num,i):
    for a in range(i+1,n):
        temp=sum1
        j=num
        temp+=arr[a]
        j+=1
        if temp/j==average:
            return True
        else:
            return find(temp,j,i+1)
    return False

arr=list(map(int,input().strip().split(',')))
n=len(arr)
sum1=sum(arr)
average=sum1/n
print(find(0,0,0))