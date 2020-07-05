t=int(input())
for i in range(t):
    n=int(input())
    l=eval('['+input().replace(' ',',')+']')
    # l.sort()
    # pos=-1
    # for j in range(len(l)):
    #     if l[j]>0:
    #         pos=j
    #         break
    # if pos==-1 or pos==0:
    #     print('No')
    #     break
    # if 0 in l:
    #     print('Yes')
    #     continue
    # else:
    #     while
    for j in range(len(l)):
        sum=0
        flag=0
        for k in range(j,len(l)):
            sum+=l[k]
            if sum==0:
                flag=1
                break
        if flag==1:
            print('Yes')
            break
    if flag==0:
        print('No')