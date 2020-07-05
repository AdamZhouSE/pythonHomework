def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    if(len(nums)==1 and nums[0]!=15 and nums[0]!=0):
        print(-1)
    elif(nums[0]==15 and len(nums)<14):
        print("DOWN")
    elif(nums[0]==0) and (len(nums)<14):
        print("UP")
    else:
        check=True
        for i in range(0,len(nums)):
            if(i+1<len(nums)):
                if(nums[i+1]-nums[i]>0):
                    if(nums[i+1]!=15):
                        check=True
                    else:
                        check=False
                elif(nums[i+1]-nums[i]<0):
                    if(nums[i+1]!=0):
                        check=False
                    else:
                        check=True
        if(nums[len(nums)-1])==15:
            check=False
        elif(nums[len(nums)-1]==0):
            check=True
        if(check):
            print("UP")
        else:
            print("DOWN")
if __name__ == "__main__":
    Test()