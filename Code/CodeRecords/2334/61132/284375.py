alist = list(map(int,input().split(',')))
l=len(alist)
if len(alist)<3:
    print(0)
else:
    rlist=[]
    maximun=0
    for i in range(l-2):
        for j in range(i+1,l-1):
            for k in range(j+1,l):
                if((alist[i]+alist[j]+alist[k])/2.0>max(alist[i],alist[j],alist[k])):
                    if(maximun<alist[i]+alist[j]+alist[k]):
                        maximun=alist[i]+alist[j]+alist[k]
    print(maximun)