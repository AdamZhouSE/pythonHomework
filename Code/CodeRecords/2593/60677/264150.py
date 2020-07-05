import re
def recursion(degree,list,start,end,answer):
    if answer.__len__()==degree:
        answerlist.append(answer[:])
        return
    for i in range(start,end):
        answer.append(str(list[i]))
        recursion(degree,list,i+1,end,answer)
        answer.remove(str(list[i]))
times=int(input())
for i in range(times):
    n=int(input())
    cnmb=input()
    if cnmb[-1]==" ":
        cnmb=cnmb[0:-1]
    nums=re.split(r'[,\s]\s*',cnmb)
    nums=[int(x) for x in nums]
    answerlist = []
    recursion(4,nums,0,n,[])
    index = []
    result=[]
    for j in range(answerlist.__len__()):
        x=answerlist[j]
        x=[int(xx) for xx in x]
        x.sort()
        if (x[0]+x[3])==(x[1]+x[2]):
            equal=x[0]+x[3]
            for k in range(4):
                index.append(nums.index(x[k]))
            index.sort()
            for k in range(2,4):
                if nums[index[0]]+nums[index[k]]==equal:
                    swap=index[1]
                    index[1]=index[k]
                    index[k]=swap
            if index[2]>index[3]:
                swap=index[2]
                index[2]=index[3]
                index[3]=swap
            index = [str(x) for x in index]
            result.append("".join(index))
            index=[]
    result.sort()
    if result.__len__()==0:
        print("no pairs")
    else:
        print(" ".join(list(result[0])))