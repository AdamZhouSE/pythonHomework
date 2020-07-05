def solution():
    n=int(input())
    inp=input().split()
    nums=[]
    for i in range(n):
        nums.append(int(inp[i]))
    sum=0
    bia=min(nums[0],nums[n-1])
    for i in range(1,n-1):
        if nums[i]>=bia:
            sum+=0
            bia=min(nums[i],max(nums[0],nums[n-1]))
        else:
            sum+=bia-nums[i]
    print(sum)

def main():
    T=int(input())
    for i in range(T):
        solution()

main()

