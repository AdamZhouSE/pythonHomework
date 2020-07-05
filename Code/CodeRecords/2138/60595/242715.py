def Test():
    nums=eval("["+input()+"]")
    k=int(input())
    print(check(nums,k))

def check(nums,target):
    for i in range(2,len(nums)+1):
        for j in range(0,len(nums)):
            if(i+j<=len(nums)):
                sum=0
                for k in range(j,i+j):
                    sum=sum+nums[k]
                if(sum%target==0):
                    return True
    return False


if __name__ == "__main__":
    Test()