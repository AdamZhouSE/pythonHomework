t=int(input())
for time in range(0,t):
    s1=input().split()
    n=int(s1[0])
    k=int(s1[1])
    nums=input().split()
    nums=list(map(int,nums))
    sums=[]
    for i in range(0,n-k+1):
        sums.append(sum(nums[i:i+k]))
    print(max(sums))
         