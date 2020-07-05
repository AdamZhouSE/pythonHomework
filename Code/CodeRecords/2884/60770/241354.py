def solve():
    height=int(input().split()[1])
    nums = list(map(int, input().split()))
    res=0
    for num1 in nums:
        for num2 in nums:
            if abs(num1-num2)<=height:
                res+=1
    res-=len(nums)
    print(res)

if  __name__ == '__main__' :
    solve()