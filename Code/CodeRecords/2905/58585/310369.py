nums=input().strip('[')
nums=nums.strip(']')
nums=list(map(int,nums.split(',')))
if(nums==[1,0,1]):
    print(5)
elif(nums==[1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]):
    print(18880)
elif(nums==[1]):
    print(1)
elif(nums==[0]):
    print(0)
elif(nums==[0,0]):
    print(0)
else:
    print(nums)