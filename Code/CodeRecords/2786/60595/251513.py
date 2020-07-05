def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    nums.sort()
    save=[]
    for x in nums:
        save.append(x)
    result=n
    jump=False
    i=1
    while(i<=n and len(nums)>1):
        temp=min(nums)
        if(i>temp):
            if(check(i,nums)):
                nums.remove(temp)
                save.remove(temp)
                i=i-1
            else:
                result=i
                jump=True
                break
        else:
            nums.remove(temp)
        i=i+1
    if(jump):
        print(result)
        print(nums)
    else:
        print(len(save))

def check(i,nums):
    for x in nums:
        if(x>=i):
            return True
    return False
if __name__ == "__main__":
    Test()