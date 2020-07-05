a=int(input())
b=int(input())
c=int(input())
nums=[a,b,c]
nums.sort()
d1,d2=nums[1]-nums[0],nums[2]-nums[1]
if(d1+d2==2):
    print([0,0])
else:
    print([1 if(min(d1,d2)<=2)else 2,d1+d2-2])
