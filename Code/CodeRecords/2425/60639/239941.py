def main():
    inp=input().split(' ')
    n=int(inp[0])
    k=int(inp[1])
    nums0=input().split(' ')
    nums=[]
    for i in range(n):
        nums.append(int(nums0[i]))
    diff=abs(nums[0]-k)
    result=nums[0]
    for i in range(1,n):
        if abs(nums[i]-k)<=diff:
            diff=abs(nums[i]-k)
            result=nums[i]
        else:
            continue
    print(result)

T=int(input())
for i in range(T):
    main()