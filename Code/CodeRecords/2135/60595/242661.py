def Test():
    nums=eval("["+input()+"]")
    x=sum(nums)//len(nums)
    s=0
    for a in nums:
        s=s+a-x
    print(s)    
if __name__ == "__main__":
    Test()