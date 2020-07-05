def sort(numlist,position,n,result):
    if(position==n):
        str = ''.join(numlist)
        if(str[0]!='0'):
            return (int)(str)&((int)(str)-1)==0

    else:
        for i in range(position,n):
            temp=numlist[i]
            numlist[i]=numlist[position]
            numlist[position]=temp
            result=sort(numlist,position+1,n,result)
            if(result==True):
                break
            temp = numlist[i]
            numlist[i] = numlist[position]
            numlist[position] =temp

        return result


nums=str(input())
numlist=[]
result=False
for i in range(0,len(nums)):
    numlist.append(nums[i])
result=sort(numlist,0,len(nums),result)
if(result==True):
    print("true")
else:
    print("false")