nums = [int(i) for i in input().split(',')]
out = ''
if(nums.count(0)>0 or nums.count(1)>0 or nums.count(2)>0):
    temp = 0
    if(nums.count(2)>0 and (nums.count(0)>0 or nums.count(1)>0 or nums.count(2)>1 or nums.count(3)>0)):
        if(nums.count(3)>0):temp =3
        elif(nums.count(2)>1):temp =2
        elif(nums.count(1)>0):temp =1
        elif(nums.count(0)>0):temp =0
        out+='2'+str(temp)+':'
        nums.remove(2)
        nums.remove(temp)
    elif( nums.count(1)>0 ):
        if(max(nums)!=1 or nums.count(1)>1):temp =max(nums)
        out+='1'+str(temp)+':'
        nums.remove(1)
        nums.remove(temp)
    if(min(nums)<6):
        if(max(nums)<6):
            out+=str(max(nums))+str(min(nums))
        else:
            out += str(min(nums)) + str(max(nums))


if(len(out)==5):print(out)
else:print('')