time=int(input())
while(time>0):
    time-=1
    strr=input()
    listt=strr.split()
    num=int(listt[0])
    step=int(listt[1])
    
    alist=[x+1 for x in range(num)]
    index=0
    while (len(alist)>1):
        index=(index+step-1)%len(alist)  # 列表的索引
        alist.pop(index)
    print(alist[0])