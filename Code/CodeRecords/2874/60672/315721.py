def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums
n=int(input())
schedule=[]
schedule=nums(input())
res=0
for i in range(len(schedule)):
    if schedule[i]==0:
        res+=1
    elif schedule[i]!=0:
        if i>=1:
            if schedule[i]==schedule[i-1] and schedule[i]!=3:
                schedule[i]=0
                res+=1
            
print(res)