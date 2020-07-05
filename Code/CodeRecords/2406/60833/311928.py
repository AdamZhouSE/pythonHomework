from _testcapi import INT_MAX
def bubble(numlist):
    length=len(numlist)
    k=0
    for i in range(0,length-1):
        for j in range(0,length-1):
            if numlist[j]>numlist[j+1]:
                temp=numlist[j]
                numlist[j]=numlist[j+1]
                numlist[j+1]=temp
                k+=1
    return k



n=int(input())
num=[]
res=INT_MAX
for i in range(0,n):
    num.append(int(input()))
for i in range(0,n-1):
    for j in range(i,n):
        if num[i]<=num[j]:
            continue
        temp=num
        k=temp[i]
        temp[i]=temp[j]
        temp[j]=k
        res=min(res,bubble(temp))
print(res)