time=int(input())
while(time>0):
    length=int(input())
    str1=input()
    listt=str1.split()
    list1=[]
    for x in listt:
        list1.append(int(x))
        
    ans=0
    
    for i in range(length):
        lmax=0
        rmax=0
        for j in range(i+1):
            lmax=max(lmax,list1[j])
        for j in range(i,length):
            rmax=max(rmax,list1[j])
        ans=ans+min(lmax,rmax)-list1[i]
    print(ans)
    time-=1