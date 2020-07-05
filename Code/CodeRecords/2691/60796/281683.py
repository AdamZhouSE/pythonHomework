def bubble(ls):
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-1-i:
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1

    return ls

def sum(ls):
    a=0
    for i in range(len(ls)):
        a=a+ls[i]
    return a
N=int(input())
result=[]
while N>0:
    n=int(input())
    ls=input().split(" ")
    ls=[int(x) for x in ls]
    ls=bubble(ls)
    #print(ls)
    s=[max(ls)]
    average=int(sum(ls)/2)
    del ls[len(ls)-1]
    now_sum=sum(s)
    while now_sum<average:
        ind=-1
        cha = abs(now_sum-average)
        for i in range(len(ls)):
            now=ls[i]+now_sum
            thischa=abs(now-average)
            if thischa<cha:
                cha=thischa
                ind=i
        if ind>=0:
            s.append(ls[ind])
            del ls[ind]
        else:
            break
        now_sum=sum(s)
    result.append(abs(now_sum-sum(ls)))
    N=N-1

for i in range(len(result)):
    print(result[i])




