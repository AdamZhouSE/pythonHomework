def findUglyNum(n,nums):
    minnum,middle,maxnum=nums[0],nums[1],nums[2]
    i,j,k=1,1,1
    arr=[]
    while len(arr)<n:
        tmp=min(minnum*i,middle*j,maxnum*k)
        if tmp==minnum*i:
            i+=1
        if tmp==middle*j:
            j+=1
        if tmp==maxnum*k:
            k+=1
        arr.append(tmp)
    return arr[n-1]


n=int(input())
a=int(input())
b=int(input())
c=int(input())
nums=[]
nums.append(a)
nums.append(b)
nums.append(c)
nums.sort()
print(findUglyNum(n,nums))