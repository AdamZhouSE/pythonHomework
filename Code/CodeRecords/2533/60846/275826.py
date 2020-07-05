def swap(nums,i,j):
    tmp=nums[i]
    nums[i]=nums[j]
    nums[j]=tmp
def sortEvenOdd(nums):
    i=0;
    j=len(nums)-1;
    n=len(nums)
    while True:
        while i<n and nums[i]%2==0:
            i+=1
        if i==n: return nums
        while j>=0 and nums[j]%2==1:
            j-=1
        if j<0: return nums
        if j<i: return nums
        swap(nums,i,j)
print(sortEvenOdd(eval(input())))