t=int(input())
for i in range(t):
    n=int(input())
    li=sorted(list(map(int,input().split())))
    k=int(input())
    l1=[]
    l2=[]
    start=0
    end=len(li)-1
    for i in range(len(li)-1):
        if li[end]+li[start]==k:
            l1.append(li[start])
            l2.append(li[end])
            end=end-1
        elif li[end]+li[start]>k:
            end-=1
        else:
            start+=1
    if len(l1)==0:
        print('-1')
    else:
        for i in range(len(l1)):
            print(str(l1[i])+' '+str(l2[i])+' '+str(k))
            