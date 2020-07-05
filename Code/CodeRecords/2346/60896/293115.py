def exec( mylist ):
    M=len(mylist)#y轴长
    N=len(mylist[0])#x轴长
    startx=0
    starty=0
    count=0
    right=True
    down=True
    x1=0#用来判断要走几个的数字
    y1=1
    while(count<M*N):
    
        if(right):#向右走
            for cx in range(0,N-x1):
                print(mylist[starty][startx],end=' ')
                count+=1
                startx+=1
            x1+=1
            startx-=1
            starty+=1
            right=False
        else:
            for cx in range(0,N-x1):
                print(mylist[starty][startx],end=' ')
                count+=1
                startx-=1
            x1+=1
            startx+=1
            starty-=1
            right=True
        if(down):
            for cy in range(0,M-y1):
                print(mylist[starty][startx],end=' ')
                count+=1
                starty+=1
            y1+=1
            starty-=1
            startx-=1
            down=False
        else:
            for cy in range(0,M-y1):
                print(mylist[starty][startx],end=' ')
                count+=1
                starty-=1
            y1+=1
            starty+=1
            startx+=1
            down=True

a=eval(input())
for i in range(0,a):
    temp=input().split(' ')
    b=map(eval,temp)
    list3=list(b)
    M=list3[0]
    N=list3[1]
    list2=[] #The list to print
    index=0
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    for i in range(0,M):
        temp=[]
        for i in range(0,N):
            temp.append(list1[index])
            index+=1
        list2.append(temp)
    exec(list2)
    print('')