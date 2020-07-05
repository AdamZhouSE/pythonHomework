if __name__=='__main__':
    nums = [int(i) for i in input().split(',')]
    m = int(input())
    left,right = max(nums) ,sum(nums)
    while left<right:
        mid = (left+right) // 2
        sums,cnt = 0,1
        for i in nums:
            if sums+i>mid:
                cnt += 1
                sums = i
            else:
                sums += i
        if cnt<=m:
            right = mid
        else:
            left = mid +1
    print(left)