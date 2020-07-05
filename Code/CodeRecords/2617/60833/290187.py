n=int(input())
for i in range(0,n):
    
    slist=input().split(' ')
    str1=slist[0]
    t=int(slist[1])
    res=0
    length=len(str1)
    for j in range(t,length+1):
        for k in range(0,length-j+1):
            temp=str1[k:k+j]
            if temp.count('1')==t:
                res+=1
    print(res)