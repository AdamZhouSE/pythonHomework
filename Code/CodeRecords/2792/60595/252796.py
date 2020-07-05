def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    result=[]
    for i in range(1,len(nums)):
        if(nums[i]-nums[i-1]!=1):
            result.append(nums[i-1])
    result.append(nums[-1])
    print(len(result))
    print(" ".join(str(x) for x in result))
if __name__ == "__main__":
    Test()