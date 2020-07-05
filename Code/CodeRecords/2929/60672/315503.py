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

nm=nums(input())
n,m=nm[0],nm[1]
after=[0 for i in range(n)]
summ=0
for i in range(n):
    num=nums(input())
    summ+=num[0]
    after[i]=num[0]-num[1]
after=sorted(after)
answer=0
for i in range(n):
    if summ>m:
        summ-=after[i]
        answer+=1
    if summ<=m:
        break
if summ<=m:
    print(answer)
else:
    answer=-1
    print(answer)