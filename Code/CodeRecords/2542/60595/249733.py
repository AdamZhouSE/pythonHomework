def Test():
    nums=eval(input())
    nums.sort()
    result=0
    for i in range(1,len(nums)+1):
        for j in range(0,len(nums)):
            if(i+j<=len(nums)):
                part=nums[j:j+i]
                if(check(part)):
                    result=max(result,len(part))
    print(result)
                
def check(x):
    for i in range(1,len(x)):
        if(x[i]-x[i-1]!=1):
            return False
    return True
if __name__ == "__main__":
    Test()