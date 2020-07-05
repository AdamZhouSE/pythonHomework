def am(nums):
    r=0
    for m in range(0,len(nums)-1):
        for n in range(m+1,len(nums)):
            temp=0
            for i in range(0,len(nums)):
                if (nums[1][1] - nums[0][1]) * nums[i][0] + (nums[1][0] - nums[0][0]) * nums[0][1] - (nums[1][1] - nums[0][1]) * nums[0][0] - (nums[1][0] - nums[0][0]) * nums[i][1] == 0:
                    temp+=1
            r=max(r,temp)
    print(r)
if __name__ == '__main__':
    am([eval('['+input()+']') for _ in range(int(input()))])
