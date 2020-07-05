#问题数
Q=int(input())
for i in range(0,Q):
    temp=input().split(" ")
    x=int(temp[0])
    y=int(temp[1])
    Big=[]
    Str=input().split()
    #创建矩阵
    for m in range(0,x):
        Small = [""] * y
        for n in range(0,y):
            Small[n]=Str[0]
            Str.pop(0)
        Big.append(Small)
    px=0#x指针
    py=0#y指针
    x0=0#x起始位置
    y0=0#y起始位置
    check=True
    while(True):
        #从左到右
        for py in range(y0,y):
            check=True
            if Big[px][py]!="":
                print(Big[px][py],end=" ")
                Big[px][py]=""
        #从上到下
        x0 = x0 + 1
        for px in range(x0, x):
            check = True
            if Big[px][py] != "":
                print(Big[px][py],end=" ")
                Big[px][py] = ""
        #从右到左
        y=y-1
        for py in range(y-1,y0-1,-1):
            check = True
            if Big[px][py] != "":
                print(Big[px][py],end=" ")
                Big[px][py] = ""
        #从下到上
        x=x-1
        for px in range(x-1, x0-1,-1):
            check = True
            if Big[px][py] != "":
                print(Big[px][py],end=" ")
                Big[px][py] = ""
        y0=y0+1
        if check==False:
            break
        check=False
    print("")
