def check(begin,end):
    index = begin+int((end - begin) / 2)

    if begin==end:
        if nums[index]==target:
            return index
        else:
            return -1
    if begin==end-1:
        if nums[begin]==target:
            return begin
        elif nums[end]==target:
            return end
        else:
            return -1
    else:
        if nums[index - 1] < nums[index] < nums[index + 1]:
            if nums[index] < target:
                return check(index+1,end)
            elif nums[index] > target:
                return check(begin,index-1)
            elif nums[index]==target:
                return index
            else:
                return -1
        elif nums[index + 1] < nums[index - 1] < nums[index]:
            if nums[index]!=target:
                return max(check(begin, index - 1), check(index + 1, end))
            else:
                return index
        else:      # nums[index]<nums[index+1]<nums[index-1]
            if nums[index]!=target:
                return max(check(begin, index - 1), check(index + 1, end))
            else:
                return index


if __name__ == '__main__':
    nums=list(map(int,input().split(",")))
    target=eval(input())
    print(check(0, len(nums) - 1))