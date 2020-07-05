def check(begin,end):
    index = begin+int((end - begin) / 2)

    if begin==end-1 or begin==end:
        if nums[begin]<=nums[end]:
            if begin==0:
                return nums[begin]
            else:
                return 1000000
        else:
            if end==len(nums)-1:
                return nums[end]
            else:
                return 1000000
    else:
        if nums[index-1]<=nums[index]<=nums[index+1]:
            return min(check(begin,index-1),check(index+1,end))
        elif nums[index + 1] < nums[index - 1] <= nums[index]:
            return nums[index+1]
        elif nums[index]<nums[index+1]<=nums[index-1]:
            return nums[index]

if __name__ == '__main__':
    nums=list(map(int,input().split(",")))
    print(check(0, len(nums) - 1))