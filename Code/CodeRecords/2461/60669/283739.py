def check(begin,end):
    index = begin+int((end - begin) / 2)

    if begin==end-1:
        if nums[begin]<nums[end]:
            return nums[begin] if begin==0 else nums[end]
        else:
            return 10000000
    else:
        if nums[index-1]<=nums[index]<=nums[index+1]:
            return min(check(begin,index-1),check(index+1,end))
        elif nums[index + 1] < nums[index - 1] < nums[index]:
            return nums[index+1]
        else:  # nums[index]<nums[index+1]<nums[index-1]
            return nums[index]

if __name__ == '__main__':
    nums=list(map(int,input().split(",")))
    print(check(0, len(nums) - 1))