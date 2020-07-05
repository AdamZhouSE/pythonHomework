
def singleNonDuplicate(nums):
    if nums[0] != nums[1]:

        return nums[0]

    if nums[len(nums)-1] != nums[len(nums)-2]:

        return nums[len(nums)-1]

    for i in range(2,len(nums)-1):

        if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:

            return nums[i]
        
if __name__ == '__main__':
    A=eval(input())
    result=singleNonDuplicate(A)
    print(result)
