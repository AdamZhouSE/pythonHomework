def Test():
    nums=eval("["+input()+"]")
    m=int(input())
    left=max(nums)
    right=sum(nums)

    def helper(mid):
        cur=0
        res=1
        for num in nums:
            cur=cur+num
            if(cur>mid):
                res=res+1
                cur=num
        return res

    while left < right:
        mid = (left + right) // 2
        if helper(mid) > m:
            left = mid + 1
        else:
            right = mid
    print(left)

if __name__ == "__main__":
    Test()
