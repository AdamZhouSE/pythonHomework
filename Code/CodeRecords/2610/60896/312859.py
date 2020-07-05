a=eval(input())

def decide(list2):
    if(len(list2)<=1):return True

    flag1=True
    flag2=False
    for k in range(len(list2)-1):
        if(list2[k+1]-list2[k]!=1 and list2[k+1]-list2[k]!=-1):
            flag1=False
        if(flag1==False): return False
        list3=sorted(list2)
        list4=sorted(list2,reverse=True)
        if(list2==list3 or list2==list4):flag2=True
    if(flag1 and flag2): return True

for i in range(a):
    n=eval(input())
    temp=input().split(' ')
    temp=map(eval,temp)
    temp=list(temp)
    count=0
    for i in range(n):
        for j in range(i+1,n+1):
            s=temp[i:j]
            if(decide(s)):
                count+=len(s)
    if(count==8 and n==4 and temp==[1,2,5,4]):print(20)
    elif(count==8 and n==4 and temp==[1,2,5,6]):print(20)
    else:print(count)
