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
string=input()
per=nums(string)
answer=round(sum(per)/n,6)
answer=str(answer)
l=list(answer)
index=l.index('.')
for i in range(6-len(answer)+3):
    answer+='0'
print(answer)