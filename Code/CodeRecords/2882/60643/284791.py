def judge(nums:[int]):
    breakPo1=len(nums)-1
    breakPo2=len(nums)-1
    if len(set(nums))==1:
        return "YES"
    elif sorted(nums)==nums:
        return "NO"
    else:
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                continue
            else:
                breakPo1=i#point1是连续常数中的第一个的位置
                break
        if breakPo1==len(nums)-1:#一直连续上升
            return "NO"

        else:
            for i in range(breakPo1,len(nums)-1):
                if nums[i+1]==nums[i]:
                    continue
                else:
                    breakPo2=i#point2是连续常数中的最后一个的位置
                    break
            if breakPo2==len(nums)-1:#没有连续下降的过程
                return "YES"

            else:#有连续下降的过程
                for i in range(breakPo2,len(nums)-1):
                    if nums[i+1]<nums[i]:
                        continue
                    else:
                        return "NO"
        return "YES"


if __name__=="__main__":
    n=int(input())
    nums=input().split()
    nums=[int(x) for x in nums]
    ans=judge(nums)
    print(ans)
