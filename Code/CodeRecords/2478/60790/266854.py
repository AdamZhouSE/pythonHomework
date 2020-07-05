t=int(input())
for i in range(0,t):
    nums=input().split()
    n1=int(nums[0])
    n2=int(nums[1])
    d=n2-n1
    k=int(input())
    print(n1+(k-1)*d)