def Test():
    nums=eval("["+input()+"]")
    m=min(nums)
    sum=0
    for n in nums:
        if(n!=m):
            sum=sum+n-m
    print(sum)

if __name__ == "__main__":
    Test()