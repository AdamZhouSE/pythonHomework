def f(li,target):
    if sum(li)<target:
        return 0
    if len(li)==0:
        return 0
    if li[len(li)-1]!=0:
        li.append(0)
    if li[0]!=0:   
        li.insert(0,0)
    li1=li[0:int(len(li)/2)]
    li2=li[int(len(li)/2):]
    length1=f(li1,target)
    length2=f(li2,target)
    s=len(li1)-1
    t=0
    x=0
    length=0
    while True:
        if x>=target:
            break
        if li1[s]>li2[t]:
            x+=li1[s]
            s-=1
            length+=1
        else:
            x+=li2[t]
            t+=1
            length+=1
    m=0
    j=[length,length1,length2]
    for k in j:
        if k!=0:
            m=k
    for k in j:
        if k!=0 and k<m:
            m=k
    return m

            
        
            
    
import sys
t=int(input())
s=[int(x) for x in input().split(',')]
print(f(s,t))


