def decid(k,num):
    k=int(k)
    num=int(num)
    ans=[]
    while num>k:
        r=num%k
        num=num//k
        ans.insert(0,r)
    ans.insert(0,num)
    return ans

num=int(input())
number=0
for i in range(2,num):
    str=decid(i,num)
    mark=0
    for j in range(0,len(str)):
        if str[j]==1:
            continue
        else:
            mark=1
            break
    if mark==0:
        number=i
        break
print(number)