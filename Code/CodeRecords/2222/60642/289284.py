def spliter(string):
    nums = []
    while(len(string) > 0):
        temp=-1
        if(string[0]=='+'):string=string[1:]
        if(string.count('+')>0):temp=string.index('+')
        if(string.count('-')>0):
            if(string.index('-')>0 and (string.index('-')<temp or temp==-1) ):
                temp=string.index('-')
            elif(string.count('-')>1 and (string[1:].index('-')<temp or temp==-1)):
                temp = string[1:].index('-')+1
        if(temp==-1):temp=len(string)
        nums.append(string[:temp])
        string= string[temp:]
    return nums

def analysis(strings,nums,sign):
    for i in strings:
        if(i[-1]!='x'):
            if (i.isdigit()):
                nums[1] -= int(i) * sign
            elif (i[1:].isdigit):
                nums[1] -= int(i) * sign
        else:
            if (len(i) == 1):
                nums[0] += sign
            elif (i[:-1].isdigit):
                nums[0] += int(i[:-1]) * sign
            elif (i[1:-1].isdigit()):
                nums[0] -= int(i[:-1]) * sign
            else:pass
    return nums

strs = input().split('=')
str1= spliter(strs[0])
str2 = spliter(strs[1])
#print(str1,str2)
nums = [0,0]
nums = analysis(str1,nums,1)
nums = analysis(str2,nums,-1)
#print(nums)
if(nums[0]==0):
    if(nums[1]==0):print('Infinite solutions')
    else:print('No solution')
else:
    print('x='+str(int(nums[1]/nums[0])))