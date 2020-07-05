n=int(input())
nums=input().split()
k=int(input())
nums=[int(x) for x in nums]
begin=2**(k-1)-1
end=n

if end>=2**k-1:
    end=2**k-1
for i in range(begin,end):
    print(nums[i],end=" ")