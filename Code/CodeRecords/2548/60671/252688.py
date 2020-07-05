time=int(input())
while(time>0):
    time-=1
    s1=input()
    num=int(input())
    list1=[]
    for x in range(len(s1)):
        for i in range(len(s1) - x):
            list1.append(s1[i:i + x + 1])
    maxl=0
    for s in list1:
        ll=list(s)
        ll.sort()
        diff=1
        for i in range(len(ll)-1):
            if(ll[i]!=ll[i+1]):
                diff+=1
        if(diff==num):
            maxl=max(maxl,len(s))
    print(maxl)
        
    