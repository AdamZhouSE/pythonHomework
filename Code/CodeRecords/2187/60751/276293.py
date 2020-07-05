num=int(input())

def sub(nums,length):
    sub_=[]
    for i in range(len(nums)-length+1):
        sub_.append(nums[i:i+length])
    return sub_

def max_(nums):
    _max = 0
    for i in nums:
        sum=0
        for j in i:
            sum+=int(j)
        if sum>_max:
            _max=sum
    return _max



for i in range(num):
    l=input().split(" ")
    M=int(l[0])
    K=int(l[1])
    nums=input().split(" ")
    print(max_(sub(nums,K)))
