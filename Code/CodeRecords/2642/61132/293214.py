l=list(eval(input()))
l.sort()
if len(l)<=2:
    print([0,0])
else:
    Max=max([l[-2]-l[0],l[-1]-l[1]])+2-len(l)
    tmp=len(l)-1
    i=0
    for j in range(len(l)):
        while l[j]-l[i]>len(l):
            i+=1
        if l[j]-l[i]+1==len(l)-1 and j-i+1==len(l)-1:
            tmp=min(2,tmp)
        else:
            tmp=min(len(l)-(j-i+1),tmp)
    print([tmp,Max])