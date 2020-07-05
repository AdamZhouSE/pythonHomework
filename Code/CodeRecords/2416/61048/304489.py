def tree2():
    str_in=input().split(' ')
    stu=[0]*int(str_in[0])
    order=int(str_in[1])
    orders=[]
    for i in range(order):
        index=int(input())-1
        stu[index]=0 if stu[index]==1 else 1
        max=0
        for j in range(len(stu)-1):
            cnt=1
            for h in range(j+1,len(stu)):
                if stu[h]!=stu[h-1]:
                    cnt+=1
                else:break
            if cnt>max:
                max=cnt
        print(max)
    return

tree2()