def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    print(nums)
    print(check(nums))
def check(nums):
    save=[]
    result=[]
    for q in nums:
        if(save.count(q)!=0):
            result.append(q)
        else:
            save.append(q)
    if(result):
        small=len(nums)
        for i in result:
            small=min(small,nums.index(i))
        return nums[small]
    else:
        return -1

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()