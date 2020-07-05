a=eval(input())
for a in range(0,a):
    length=eval(input())
    list1=input().split(' ')
    b=map(eval,list1)
    list2=list(b) #转整数列表
    count=0 #计数
    for i in range(0,length-2):
        x1=list2[i]
        for m in range(i+1,length-1):
            x2=list2[m]
            for n in range(m+1,length):
                x3=list2[n]
                if(x1+x2>x3 and x1+x3>x2 and x2+x3>x1): count+=1
    print(count)