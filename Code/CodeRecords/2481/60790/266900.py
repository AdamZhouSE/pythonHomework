t=int(input())
for i in range(0,t):
    mn=input().split()
    n=int(mn[0])
    m=int(mn[1])
    s1=input().split()
    s2=input().split()
    set1=set(s1)
    set2=set(s2)
    s1=list(set1)
    s2=list(set2)
    count=0
    for i in s1:
        if(i in s2):
            count+=1
    print(count)